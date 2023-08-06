import re

from typing import List

from enginelib.rds.client import db_client, db_name
from enginelib.errors import Error

_bad_chars = re.compile(r'[^0-9a-zA-z\-_]')


def sql_sanitize(text: str) -> str:
    return _bad_chars.sub("", text)


def run_query(tx_id: str, query: str) -> List:
    rows, error = db_client.GetReferenceData(tx_id or "<no_tx_id>", query)
    if not error:
        return rows
    elif 'does not exist' in error:
        return []
    raise Error(f"Unable to query {db_name}, error: {str(error)}")
