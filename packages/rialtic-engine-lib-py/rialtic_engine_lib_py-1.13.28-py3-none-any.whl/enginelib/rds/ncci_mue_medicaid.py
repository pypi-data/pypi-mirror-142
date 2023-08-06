import functools

from enginelib.rds.client import db_name

from enginelib.rds.utils import sql_sanitize, run_query

from typing import Dict


class NCCIMueMedicaid:
    @staticmethod
    @functools.lru_cache(None)
    def get_row(tx_id: str, proc_code: str) -> Dict:
        """return single row from ncci_mue_mcr table, matching proc_code"""
        query = f'''
            SELECT * FROM "{db_name}".ncci_mue_mcd
            WHERE hcpcs = '{sql_sanitize(proc_code)}'
        '''
        rows = run_query(tx_id, query)
        if rows:
            return rows[0]
        else:
            return {}
