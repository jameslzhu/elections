from __future__ import unicode_literals
import datetime
import calendar

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

# Infosession spreadsheet
INFOSESSION_SPREADSHEET_ID = '183nO7sBKIlveaieqobYuS8io3ztGLZnL2RMyfee1b38'

##########################################
#  Variables to edit each semester       #
##########################################

# Sanity Check to make sure stuff is updated before running
"""
Please modify fields that need to be modified, then
modify this section as confirmation

You may choose to override with DATE_SANITY_OVERRIDE
"""
DATE_SANITY_OVERRIDE = False

RECENT_CAND_MONTH = 12    # Take month and year of most recent semester
RECENT_CAND_YEAR = 2020   #  Candidate Initiation (on the dot)
                          # Normally, Fall is 12 (December), Spring is 5 (May)

NEXT_CAND_MONTH = 5       # Take month and year estimate of next semester
NEXT_CAND_YEAR = 2021     #  Candidate Initiation (on the dot)
                          # Normally, Fall Candidate Semester is: April (4) or May (5)
# Will use end of the month of "Month - 1" by the way (with 1 - 1 ==> 12)

COMPSERV_OFFICERS = "Oscar Chan, Sam Maher, Alvin Xu, Jeffrey Deng"
COMPSERV_AOS = "Haolin Zhu, Sid Ijju"

NEW_OFFICER_SHEET = 'New Officers Sp21'
# OLD_OFFICER_SHEET = 'Returning Officers'
MEMBER_SHEET = 'New Members Sp21'
INFOSESSIONS_SHEET = 'Form Responses 1'

NEW_OFFICER_SHEET_ID = '1885638305'
# OLD_OFFICER_SHEET_ID = '682750401'
MEMBER_SHEET_ID = '1338093122'

# You probably don't have to edit this one as often
INFOSESSIONS_SHEET_ID = '1100426286'
##########################################
#                                        #
##########################################


NEW_OFFICER_RANGE = '\'{}\'!A:G'.format(NEW_OFFICER_SHEET)
#OLD_OFFICER_RANGE = '\'{}\'!A:F'.format(OLD_OFFICER_SHEET)
MEMBER_RANGE = '\'{}\'!A:F'.format(MEMBER_SHEET)
INFOSESSION_RANGE = '\'{}\'!A:E'.format(INFOSESSIONS_SHEET)

## DATE SANITY CHECK FUNCTIONS
##### Don't touch below functions unless necessary
def create_time_range(start_month, start_year, end_month, end_year):
    end_month = (end_month - 1) % 12
    if end_month == 0:
        end_month = 12
    start_day = calendar.monthrange(start_year, start_month)[0]
    end_day = calendar.monthrange(end_year, end_month)[1]
    date_time_start = datetime.datetime(year=start_year, month=start_month, day=start_day)
    date_time_end   = datetime.datetime(year=end_year, month=end_month, day=end_day)
    return date_time_start, date_time_end

def date_sanity_check(assert_out=True):
    if DATE_SANITY_OVERRIDE:
        print("Date checking has been overrided. Date is not checked")
        return True
    time_now = datetime.datetime.now()
    date_time_start, date_time_end = create_time_range(RECENT_CAND_MONTH, RECENT_CAND_YEAR, \
                                                       NEXT_CAND_MONTH, NEXT_CAND_YEAR)
    result = date_time_start < time_now and time_now < date_time_end
    if assert_out:
        assert result, "Outside of current sanity check date range. Please check election/settings.py and make sure you have changed what you needed to change and reset the dates."
    return result

date_sanity_check()
