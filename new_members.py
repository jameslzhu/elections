# @author: Catherine Hu, James Zhu, Carolyn Wang (for add_users)

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from hknlib.election.settings import MEMBER_RANGE

from hknlib.election.cred import get_credentials
from hknlib.election.sheets import get_election_data
from hknlib.election.users import add_users
from hknlib.election.groups import add_members_to_committes

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
