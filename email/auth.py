from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import argparse

from googleapiclient.discovery import build
from google.oauth2 import service_account
from .settings import SCOPES

def get_service(service_account_file):
    creds = service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=SCOPES,
            subject="hkn-ops@hkn.eecs.berkeley.edu")
    return build('gmail', 'v1', credentials=creds)