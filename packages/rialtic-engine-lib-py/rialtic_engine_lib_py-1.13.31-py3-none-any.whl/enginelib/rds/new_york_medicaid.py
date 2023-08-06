from typing import Set
import datetime as dt

from enginelib.rds.client import db_client, db_name
from enginelib.errors import Error

from enginelib.rds.utils import sql_sanitize


class NewYorkMedicaid:
    @staticmethod
    def query_lab_codes(code: str, start_date: dt.date, transaction_id: str) -> Set[str]:
        # noinspection SqlResolve,SqlDialectInspection,SqlNoDataSourceInspection
        query = f'''
            SELECT code, effective_start_date, effective_end_date
            FROM {db_name}.mcd_ny_lab_fees
            WHERE code = '{sql_sanitize(code)}';
        '''
        records, err = db_client.GetReferenceData(transactionId=transaction_id, query=query)
        if err:
            raise Error(f"Unable to query NY MCD Lab Fees, error: {str(err)}")
        return {rec['code'] for rec in (records or []) if
                rec['effective_start_date'] <= start_date.strftime("%Y-%m-%d") < str(rec['effective_end_date'])}
