from pprint import pprint

from hknlib.election.constants import ELECTION_SPREADSHEET_ID, NEW_OFFICER_RANGE
from hknlib.election.google_utils import get_sheet_data
from hknlib.election.users import add_users
from hknlib.election.groups import add_officers_to_committes, add_members_to_committes


def main():
    election_data = get_sheet_data(NEW_OFFICER_RANGE, ELECTION_SPREADSHEET_ID)

    pprint(election_data[-1:])
    proceed = input("Above is the most recent entry. Does this look correct? [y/n]\n")
    if proceed != "y": return

    add_users(election_data)
    add_officers_to_committes(election_data)
    add_members_to_committes(election_data)


if __name__ == "__main__":
    main()
