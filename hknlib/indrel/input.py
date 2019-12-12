from .settings import SPREADSHEET_ID, SENDER, DEBUG
from .company import Company

def get_companies(service, sheet_range):
    companies = []
    if DEBUG:
        test_company = Company("Google", "anthonyding@berkeley.edu", False)
        companies.append()
    else:
        # TODO: generate company list from sheet
    return companies

def generate_message_body(company):
    if "@hkn.eecs.berkeley.edu" not in SENDER:
        raise Exception("sender email (found in hknlib.indrel.settings) is not a valid HKN email address")
    if company.cap():
        return generate_cap_message_body(company)
    

def generate_cap_message_body(company):
    pass