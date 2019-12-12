from .settings import SPREADSHEET_ID, SENDER
from .company import Company

def get_companies(service, sheet_range):
    pass

def multipart_file_path():
    pass

def generate_message_body(company):
    if "@hkn.eecs.berkeley.edu" not in SENDER:
        raise Exception("sender email (found in hknlib.indrel.settings) is not a valid HKN email address")