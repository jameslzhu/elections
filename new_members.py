# @author: Catherine Hu, James Zhu, Carolyn Wang (for add_users)

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from pprint import pprint

from hknlib.election.settings import ELECTION_SPREADSHEET_ID, MEMBER_RANGE

from hknlib.election.cred import get_credentials
from hknlib.election.sheets import get_sheet_data
from hknlib.election.users import add_users
from hknlib.election.groups import add_members_to_committes


def main():
    credentials = get_credentials("./secret/hknlib.json")

    election_data = get_sheet_data(credentials, MEMBER_RANGE, ELECTION_SPREADSHEET_ID)
    # TODO FIXME HACK
    for line in election_data:
        line.insert(5, "")

    pprint(election_data[-1:])
    proceed = input("Above is the most recent entry. Does this look correct? [y/n]\n")
    if proceed != "y": return

    add_users(credentials, election_data)
    add_members_to_committes(credentials, election_data)


if __name__ == '__main__':
    main()
