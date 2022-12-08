import os
import json

from hknlib import ROOT_DIR


SCOPES = [
    "https://www.googleapis.com/auth/admin.directory.group.member",
    "https://www.googleapis.com/auth/admin.directory.user",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/admin.directory.group",
    "https://www.googleapis.com/auth/gmail.send",
]

API_KEY_PATH = "secret/hknlib.key"

HKN_DOMAIN = "@hkn.eecs.berkeley.edu"
EMAIL_SENDER = "hkn-ops@hkn.eecs.berkeley.edu"

ELECTION_SPREADSHEET_ID = "1wnZfinKlVUsdXaz-W0ACnb_G7HFfDVlpudUSGpA1GrM"

current_semester_settings = json.load(open(os.path.join(ROOT_DIR, "config", "settings.json")))

COMPSERV_OFFICERS = current_semester_settings["compserv"]["officers"]
COMPSERV_AOS = current_semester_settings["compserv"]["aos"]

NEW_OFFICER_SHEET = current_semester_settings["new officer sheet"]["name"]
NEW_OFFICER_SHEET_ID = current_semester_settings["new officer sheet"]["id"]
NEW_OFFICER_RANGE = '\'{}\'!A:G'.format(NEW_OFFICER_SHEET)

MEMBER_SHEET = current_semester_settings["new member sheet"]["name"]
MEMBER_SHEET_ID = current_semester_settings["new member sheet"]["id"]
MEMBER_RANGE = '\'{}\'!A:F'.format(MEMBER_SHEET)
