from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import argparse

# from oauth2client import file, client, tools
from google.oauth2 import service_account
from google_auth_oauthlib.flow import Flow
from .settings import CREDENTIALS_FILE, CLIENT_SECRET_FILE, SCOPES, APPLICATION_NAME

parser = argparse.ArgumentParser(parents=[tools.argparser])
flags = parser.parse_args()

# If modifying these scopes, delete your previously saved credentials
# at CREDENTIALS_FILE
def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credentials = service_account.Credentials.from_service_account_file(CLIENT_SECRET_FILE)
    scoped_credentials = credentials.with_scopes(SCOPES)

    # Create the flow using the client secrets file from the Google API
    # Console.
    flow = Flow.from_client_secrets_file(
        'path/to/client_secrets.json',
        scopes=['profile', 'email'],
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')

    # Tell the user to go to the authorization URL.
    auth_url, _ = flow.authorization_url(prompt='consent')

    print('Please go to this URL: {}'.format(auth_url))

    # The user will get an authorization code. This code is used to get the
    # access token.
    code = input('Enter the authorization code: ')
    flow.fetch_token(code=code)

    # You can use flow.credentials, or you can just get a requests session
    # using flow.authorized_session.
    session = flow.authorized_session()
    print(session.get('https://www.googleapis.com/userinfo/v2/me').json())

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
