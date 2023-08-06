import datetime as dt
from typing import List, Dict

from enginelib.claim_line_focus import ClaimLineFocus
from enginelib.errors import Error
from enginelib.rds.client import db_client, db_name


class NCCIPTPMedicare:
    @staticmethod
    def fetch_rows_in_ncci_ptp_mcr(clf: ClaimLineFocus) -> List[Dict[str, str]]:
        """
        Returns:
            list of rows in reference data set NCCI_PTP_MCR with
            the given procedureCode in column 2 and within the
            prescribed effective date range:

            EFFECTIVE_DATE <= DATE < DELETION_DATE
        """
        
        from_date = clf.service_period.start
        formatted_date = dt.datetime(from_date.year, from_date.month, from_date.day).strftime("%Y-%m-%d")

        # noinspection SqlDialectInspection, SqlNoDataSourceInspection
        query = f'''
            SELECT *
            FROM {db_name}.ncci_ptp_mcr WHERE "column2" = '{clf.procedure_code}' AND 
            "file_effective_begin" <= '{formatted_date}'::date AND "file_effective_end" >= '{formatted_date}'::date ;
        '''

        ref_data, err = db_client.GetReferenceData(clf.request.transaction_id or 'testing', query)
        if err is not None:
            raise Error(f"Error fetching data from NCCI PTP Medicare reference data set. "
                        f"GetReferenceData() returned error '{str(err)}'.")

        start_date = clf.service_period.start
        relevant_ref_data = list()
        for entry in ref_data or list():
            effective_date = (entry.get('effective_date') or '1900-01-01') .split('T')[0]
            deletion_date = (entry.get('deletion_date') or '9999-12-31').split('T')[0]
            if (dt.datetime.strptime(effective_date, '%Y-%m-%d').date() <= start_date
                    < dt.datetime.strptime(deletion_date, '%Y-%m-%d').date()):
                relevant_ref_data.append(entry)

        return relevant_ref_data
