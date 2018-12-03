from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import argparse

from oauth2client import file, client, tools
from .settings import CREDENTIALS_FILE, CLIENT_SECRET_FILE, SCOPES, APPLICATION_NAME

parser = argparse.ArgumentParser(parents=[tools.argparser])
flags = parser.parse_args()

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/admin-directory_v1-python-quickstart.json
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
