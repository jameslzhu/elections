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
RECENT_CAND_YEAR = 2021   #  Candidate Initiation (on the dot)
                          # Usually, this is when new officers are elected
                          # Normally, during the Fall   is 12 (December),
                          #           during the Spring is  5 (May)
# Script will look at this as the START of the month and year listed

NEXT_CAND_MONTH = 5       # Take month and year estimate of NEXT semester
NEXT_CAND_YEAR = 2022     #  Candidate Initiation (on the dot)
                          # Example, current Semester is Fall, then use the Spring date here
                          #             OR
                          #          current Semester is Spring, then use the Fall date here
# Will use END of the month of "Month - 1" by the way (with 1 - 1 ==> 12)

COMPSERV_OFFICERS = "Oscar Chan, Brian Yu, Anthony Maltsev, Anirban Sarkar"
COMPSERV_AOS = "Sam Maher, Yousef Helal, Justin Zhang"

NEW_OFFICER_SHEET = 'New Officers Sp22'
# OLD_OFFICER_SHEET = 'Returning Officers'
MEMBER_SHEET = 'New Members Sp22'

NEW_OFFICER_SHEET_ID = '272309335'
# OLD_OFFICER_SHEET_ID = '682750401'
MEMBER_SHEET_ID = '1002817381'
##########################################
#                                        #
##########################################


NEW_OFFICER_RANGE = '\'{}\'!A:G'.format(NEW_OFFICER_SHEET)
#OLD_OFFICER_RANGE = '\'{}\'!A:F'.format(OLD_OFFICER_SHEET)
MEMBER_RANGE = '\'{}\'!A:F'.format(MEMBER_SHEET)

## DATE SANITY CHECK FUNCTIONS
##### Don't touch below functions unless necessary
def create_time_range(start_month, start_year, end_month, end_year):
    end_month = (end_month - 1) % 12
    if end_month == 0:
        end_month = 12
    start_day = 1
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
    result = date_time_start <= time_now and time_now <= date_time_end
    if assert_out:
        assert result, "Outside of current sanity check date range. Please check election/settings.py and make sure you have changed what you needed to change and reset the dates."
    return result

date_sanity_check()
