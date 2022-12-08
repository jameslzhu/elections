from __future__ import unicode_literals

SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.group.member',
    'https://www.googleapis.com/auth/admin.directory.user',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/admin.directory.group',
    'https://www.googleapis.com/auth/gmail.send'
]

# Stores API key
SERVICE_ACCOUNT_FILE = 'secret/service.json'

# Elections spreadsheet
ELECTION_SPREADSHEET_ID = '1wnZfinKlVUsdXaz-W0ACnb_G7HFfDVlpudUSGpA1GrM'

##########################################
#  Variables to edit each semester       #
##########################################

COMPSERV_OFFICERS = "Franz Kieviet, Maxwell Lo, Shawn Zhao, Addison Kalanther"
COMPSERV_AOS = "Brian Yu, Will Giorza"

NEW_OFFICER_SHEET = 'New Officers Sp23'
MEMBER_SHEET = 'New Members Sp23'

NEW_OFFICER_SHEET_ID = '1414929723'
MEMBER_SHEET_ID = '103966474'

##########################################
#                                        #
##########################################


NEW_OFFICER_RANGE = '\'{}\'!A:G'.format(NEW_OFFICER_SHEET)
MEMBER_RANGE = '\'{}\'!A:F'.format(MEMBER_SHEET)
