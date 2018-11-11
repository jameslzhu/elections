"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
# @author: Catherine Hu, James Zhu
from apiclient.discovery import build
from oauth2client import file, client, tools

import httplib2
import os

import argparse
flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/admin-directory_v1-python-quickstart.json
SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.group.member',
    'https://www.googleapis.com/auth/admin.directory.user',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
]
CLIENT_SECRET_FILE = 'client_secret.json'
CREDENTIALS_FILE = 'cred.json'
APPLICATION_NAME = 'hknweb'

# Elections spreadsheet
SPREADSHEET_ID = '1wnZfinKlVUsdXaz-W0ACnb_G7HFfDVlpudUSGpA1GrM'
OFFICER_SHEET_ID = '682750401'
MEMBER_SHEET_ID = '2002556869'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_dir = os.getcwd()
    credential_path = os.path.join(credential_dir, CREDENTIALS_FILE)

    store = file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
    return credentials


def get_election_data(credentials, range):
    # Setup the Sheets API
    http = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http=http)

    # Call the Sheets API
    result = service.spreadsheets().values() \
        .get(spreadsheetId=SPREADSHEET_ID, range=range) \
        .execute()
    return result.get('values', [])


def get_users(credentials):
    http = credentials.authorize(httplib2.Http())
    service = build('admin', 'directory_v1', http=http)

    print('Getting the first 10 users in the domain')
    results = service.users() \
        .list(customer='my_customer', maxResults=10, orderBy='email') \
        .execute()
    return results.get('users', [])

def add_user_to_group(credientials, user, group):
    #add USER to a mail list GROUP
    http = credentials.authorize(httplib2.Http())
    service = build('admin', 'directory_v1', http=http)
    return service.members().insert(groupKey=group, body=user).execute()

def add_all_to_groups(credentials):
    # add all users to all mailing lists
    credentials = get_credentials()
    election_data = get_election_data(credentials)
    users = get_users(credentials)

    mailing_lists = {}
    if election_data:
        for i in range(0, election_data.length)
            row = election_data[i]
            mailing_list = row[6][:-1].split('@, ')
            mailing_list[users[row]] = mailing_list

    for user, mailing_list in mailing_lists.items()
        for group in mailing_list
            add_user_to_group(credentials, user, group) 


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
        print(user['primaryEmail'].split('@')[0])
        # print('{0} ({1})'.format(user['primaryEmail'], user['name']['fullName']))


if __name__ == '__main__':
    main()
