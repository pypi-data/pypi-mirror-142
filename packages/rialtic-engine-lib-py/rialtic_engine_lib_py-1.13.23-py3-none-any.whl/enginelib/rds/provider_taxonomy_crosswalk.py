from typing import List, Set

from enginelib.rds.client import db_name, db_client
from enginelib.errors import Error

from functools import lru_cache


class RialticDataInterfaceError(Error):
    def __init__(self, message="there was a problem while fetching reference data"):
        super().__init__(f'Error: {message}')


class ProviderTaxonomyCrosswalk:
    @staticmethod
    @lru_cache()
    def medicare_specialty_code(taxonomy: str) -> str:
        # noinspection SqlNoDataSourceInspection,SqlDialectInspection
        query = f'''SELECT "medicare_specialty_code" 
            FROM {db_name}.ptxw_records 
            WHERE "provider_taxonomy_code"='{taxonomy}' 
        LIMIT 1;
        '''

        try:
            records, err = db_client.GetReferenceData('transaction_id', query)
            records = records or list()
            if records:
                return records[0]['medicare_specialty_code'].strip()

        except (IndexError, KeyError, TypeError):
            pass

        raise Error('Could not fetch data from Provider Taxonomy Crosswalk'
                    f' reference data set for taxonomy code {taxonomy}.')

    @staticmethod
    @lru_cache()
    def taxonomy_codes_for(specialty: str) -> List[str]:
        # noinspection SqlNoDataSourceInspection,SqlDialectInspection
        query = f'''
            SELECT "provider_taxonomy_code" 
                FROM {db_name}.ptxw_records 
                WHERE "medicare_specialty_code"='{specialty}' 
            '''

        try:
            records, err = db_client.GetReferenceData('transaction_id', query)
            if records:
                return [record['provider_taxonomy_code'].strip() for record in records or list()]

        except (IndexError, KeyError, TypeError):
            pass

        raise Error(f'Could not fetch data from Provider Taxonomy Crosswalk'
                    f' reference data set for specialty code {specialty}.')

    @staticmethod
    @lru_cache()
    def get_taxonomy_groups(taxonomy_code: str) -> Set[str]:
        # taxonomy code is unique alphanumeric and has length 10
        if not (taxonomy_code.isalnum() and len(taxonomy_code) == 10):
            return set()

        # noinspection SqlNoDataSourceInspection,SqlDialectInspection
        query = (
            f'SELECT "medicare_specialty_code" '
            f'FROM {db_name}.ptxw_records '
            f"WHERE \"provider_taxonomy_code\"='{taxonomy_code}'"
        )
        ref_data, err = db_client.GetReferenceData("not_available", query)
        if err:
            raise RialticDataInterfaceError(message=str(err))
        if ref_data:
            return {r["medicare_specialty_code"] for r in ref_data}
        else:
            return set()

    @classmethod
    @lru_cache()
    def is_taxonomy_code_valid(cls, taxonomy_code: str) -> bool:
        return bool(cls.get_taxonomy_groups(taxonomy_code))
