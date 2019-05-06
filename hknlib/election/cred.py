from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os
import argparse

from google.oauth2 import service_account
from .settings import SCOPES

def get_credentials(service_account_file):
    # Source: https://developers.google.com/identity/protocols/OAuth2ServiceAccount
    return service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=SCOPES,
            subject="hkn-ops@hkn.eecs.berkeley.edu")
