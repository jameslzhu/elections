from typing import List

from tqdm import tqdm

from hknlib.election.constants import HKN_DOMAIN
from hknlib.election.google_utils import build_directory_service


def add_user_to_group(user, groupKey) -> None:
    user = user.strip()
    email = f"{user}{HKN_DOMAIN}"
    group = f"{groupKey}{HKN_DOMAIN}"

    service = build_directory_service()

    response = service.members().hasMember(groupKey=group, memberKey=email).execute()
    if response["isMember"]:
        return

    body = {
        "email": email,
        "role": "MEMBER",
    }
    service.members().insert(groupKey=group, body=body).execute()


def add_officers_to_committes(election_data: List[List[str]]):
    missing_data = lambda row: len(row) < 6
    no_committee = lambda row: row[5] == "N/A"
    get_groups = lambda committee: [f"{committee}-officers", f"current-{committee}"]

    for row in tqdm(election_data, desc="Adding officers to committees"):
        if missing_data(row) or no_committee(row):
            continue

        user = row[3]
        committee = row[5].strip("@")

        for group in get_groups(committee):
            add_user_to_group(user, group)


def add_members_to_committes(election_data):
    for row in tqdm(election_data, "Adding members to committees"):
        if len(row) < 7:
            continue

        user = row[3]
        groups = row[6][:-1].split("@, ")

        for group in groups:
            add_user_to_group(user, group)
