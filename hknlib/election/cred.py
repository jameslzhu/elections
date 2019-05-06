from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import argparse

from google.oauth2 import service_account
from .settings import SERVICE_ACCOUNT_FILE, SCOPES

def get_credentials():
    # Source: https://developers.google.com/identity/protocols/OAuth2ServiceAccount
    return service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
