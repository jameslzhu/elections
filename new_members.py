# @author: Catherine Hu, James Zhu, Carolyn Wang (for add_users)

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from election.settings import (
    SCOPES,
    CLIENT_SECRET_FILE,
    CREDENTIALS_FILE,
    APPLICATION_NAME,
    SPREADSHEET_ID,
    MEMBER_RANGE,
)

from election.cred import get_credentials
from election.sheets import get_election_data
from election.users import add_users
from election.groups import add_members_to_committes

# test_data = [
#     ['12/2/2018 22:24:44', 'Test', 'User', 'test_user', 'jameszhu@hkn.eecs.berkeley.edu', 'compserv@'],
# ]

def main():
    credentials = get_credentials()
    election_data = get_election_data(credentials, MEMBER_RANGE)
    # TODO FIXME HACK
    for line in election_data:
        line.insert(5, "")
    # print(election_data[0])
    add_users(credentials, election_data)
    add_members_to_committes(credentials, election_data)

if __name__ == '__main__':
    main()
