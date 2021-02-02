from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from googleapiclient.discovery import build

def get_sheet_data(credentials, range, spreadsheet_id):
    # Setup the Sheets API
    service = build('sheets', 'v4', credentials=credentials)
    # Call the Sheets API
    result = service.spreadsheets().values() \
        .get(spreadsheetId=spreadsheet_id, range=range) \
        .execute()
    return result.get('values', [])[1:]
