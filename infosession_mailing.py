# @author: Catherine Hu, James Zhu, Carolyn Wang (for add_users), Oscar Chan

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from hknlib.election.settings import INFOSESSION_RANGE, INFOSESSION_SPREADSHEET_ID

from hknlib.election.cred import get_credentials
from hknlib.election.sheets import get_sheet_data
from hknlib.election.users import add_users
from hknlib.election.groups import add_email_to_group

# test_data = [
#     ['12/2/2018 22:24:44', 'EMAIL@berkeley.edu', 'EECS', 'EMAIL@berkeley.edu', 'Yes'],
# ]

def main():
    credentials = get_credentials("./secret/hknlib.json")
    mailing_list = get_sheet_data(credentials, INFOSESSION_RANGE, INFOSESSION_SPREADSHEET_ID)
    for row in mailing_list:
        if len(row) != 5:
            print("Skipped row:", row)
            continue
        form_fill_email = row[1] # Field currently not used
        majors = row[2]          # Field currently not used
        email = row[3]
        consent = (row[4] == "Yes")
        if consent:
            status = add_email_to_group(credentials, email, 'infosessions')
            if not status:
                print("Email already added:", email)
        else:
            print("User did not consent:", row)

if __name__ == '__main__':
    main()
