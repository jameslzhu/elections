"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
from apiclient.discovery import build
from oauth2client import file, client, tools

import httplib2
import os

import argparse
flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/admin-directory_v1-python-quickstart.json
SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.user',
    'https://www.googleapis.com/auth/spreadsheets.readonly'
]
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'hknweb'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_dir = os.getcwd()
    credential_path = os.path.join(credential_dir, 'cred.json')

    store = file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
    return credentials


def get_election_data(credentials):
    # Setup the Sheets API
    http = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http=http)

    # Call the Sheets API
    SPREADSHEET_ID = '1rAqIaxe138yzQ0uS5LKecvnz5wUVpUcaJzm0eh4c04w'
    SEMESTER = 'Fall'
    YEAR = '2018'
    RANGE_NAME = '{} {}!A2:G16'.format(SEMESTER, YEAR)
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                 range=RANGE_NAME).execute()
    return result.get('values', [])


def get_users(credentials):
    http = credentials.authorize(httplib2.Http())
    service = build('admin', 'directory_v1', http=http)

    print('Getting the first 10 users in the domain')
    results = service.users().list(customer='my_customer', maxResults=10,
                                   orderBy='email').execute()
    return results.get('users', [])
    

def main():
    """Shows basic usage of the Google Admin SDK Directory API.

    Creates a Google Admin SDK API service object and outputs a list of first
    10 users in the domain.
    """
    credentials = get_credentials()
    election_data = get_election_data(credentials)
    users = get_users(credentials)

    print('Position, Officers')
    if election_data:
        for row in election_data:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('{}, {}'.format(row[0], row[1:]))

    print('Users:')
    for user in users:
        print('{0} ({1})'.format(user['primaryEmail'], user['name']['fullName']))


if __name__ == '__main__':
    main()
