from pprint import pprint

from hknlib.election.constants import ELECTION_SPREADSHEET_ID, MEMBER_RANGE
from hknlib.election.google_utils import get_sheet_data
from hknlib.election.users import add_users
from hknlib.election.groups import add_members_to_committes


def main():
    election_data = get_sheet_data(MEMBER_RANGE, ELECTION_SPREADSHEET_ID)
    # TODO FIXME HACK
    for line in election_data:
        line.insert(5, "")

    pprint(election_data[-1:])
    proceed = input("Above is the most recent entry. Does this look correct? [y/n]\n")
    if proceed != "y": return

    add_users(election_data)
    add_members_to_committes(election_data)


if __name__ == "__main__":
    main()
