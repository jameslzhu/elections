from typing import List

from google.oauth2 import service_account
from googleapiclient.discovery import build

from hknlib.election.constants import SCOPES, EMAIL_SENDER, API_KEY_PATH


def get_credentials(service_account_file):
    # Source: https://developers.google.com/identity/protocols/OAuth2ServiceAccount
    return service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=SCOPES,
            subject=EMAIL_SENDER)


credentials = get_credentials(API_KEY_PATH)


def get_sheet_data(range: str, spreadsheet_id: str) -> List[List[str]]:
    # Setup the Sheets API
    service = build("sheets", "v4", credentials=credentials)

    # Call the Sheets API
    result = service.spreadsheets().values() \
        .get(spreadsheetId=spreadsheet_id, range=range) \
        .execute()

    return result.get("values", [])[1:]


def build_directory_service():
    return build("admin", "directory_v1", credentials=credentials)


def build_gmail_service():
    return build("gmail", "v1", credentials=credentials)
