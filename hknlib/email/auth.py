from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import argparse

from googleapiclient.discovery import build
from google.oauth2 import service_account
from .settings import SCOPES

def get_gmail_service(service_account_file):
    creds = get_credentials(service_account_file)
    return build('gmail', 'v1', credentials=creds)

def get_sheets_service(service_account_file):
    creds = get_credentials(service_account_file)
    return build('sheets', 'v4', credentials=credentials)

def get_credentials(service_account_file):
    return service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=SCOPES,
            subject="hkn-ops@hkn.eecs.berkeley.edu")
        