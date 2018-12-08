from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import httplib2
from google.auth.transport.requests import AuthorizedSession
from apiclient.discovery import build
from googleapiclient.discovery import build

from .settings import SPREADSHEET_ID

def get_election_data(credentials, range):
    # Setup the Sheets API
    service = build('sheets', 'v4', credentials=credentials)
    # Call the Sheets API
    result = service.spreadsheets().values() \
        .get(spreadsheetId=SPREADSHEET_ID, range=range) \
        .execute()
    return result.get('values', [])[1:]
