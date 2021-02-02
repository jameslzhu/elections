# @author: Catherine Hu, James Zhu, Carolyn Wang (for add_users)

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from hknlib.election.settings import ELECTION_SPREADSHEET_ID, NEW_OFFICER_RANGE

from hknlib.election.cred import get_credentials
from hknlib.election.sheets import get_sheet_data
from hknlib.election.users import add_users
from hknlib.election.groups import add_all_to_committes

# test_data = [
#     ['12/2/2018 22:24:44', 'Test', 'User', 'test_user', 'jameszhu@hkn.eecs.berkeley.edu', 'compserv@'],
# ]

def main():
    credentials = get_credentials("./secret/hknlib.json")
    election_data = get_sheet_data(credentials, NEW_OFFICER_RANGE, ELECTION_SPREADSHEET_ID)
    #print(election_data)
    add_users(credentials, election_data)
    add_all_to_committes(credentials, election_data)

if __name__ == '__main__':
    main()
