from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .settings import ELECTION_SPREADSHEET_ID

HKN_DOMAIN = '@hkn.eecs.berkeley.edu'

def add_user_to_group(credentials, user, groupKey, hkn_username=True):
    #add USER to a mail list GROUP
    user_email = user.strip()
    
    user_email = user + HKN_DOMAIN
    
    add_email_to_group(credentials, user_email, groupKey, email_list=False, user=user)

def add_email_to_group(credentials, email, groupKey, email_list=True, user=None):
    if user is None:
        user = email
    
    service = build('admin', 'directory_v1', credentials=credentials)
    
    email = email.strip()

    body = {
        'email': email,
        'role': 'MEMBER',
    }
    group = groupKey + HKN_DOMAIN
    if not email_list:
        response = service.members().hasMember(groupKey=group, memberKey=body.get('email')).execute()
        if response['isMember']:
            return False
    try:
        _ = service.members().insert(groupKey=group, body=body).execute()
        print("{}->{}".format(user, groupKey))
    except HttpError as e:
        if e.resp.status == 409 and e._get_reason().strip() == "Member already exists.":
            return False
        else:
            print(body)
            print(e.resp.status, e._get_reason().strip())
            print("")
            raise e
    return True


def add_officers_to_committes(credentials, election_data):
    user_committee = []
    if election_data:
        for i in range(0, len(election_data)):
            if len(election_data[i]) < 6:
                continue
            committee = election_data[i][5]
            if committee == "N/A":
                continue
            if committee[-1:] == "@":
                committee = committee[:-1]
            user_committee.append((election_data[i][3], committee))
            #user_committee[users[i]] = committee

    for user, committee in user_committee:
        result = add_user_to_group(credentials, user, committee+'-officers')
        result = add_user_to_group(credentials, user, "current-"+committee)


def add_members_to_committes(credentials, election_data):
    mailing_lists = []
    if election_data:
        for i in range(0, len(election_data)):
            if len(election_data[i]) < 7:
                continue
            row = election_data[i]
            mailing = row[6][:-1].split('@, ')
            mailing_lists.append((election_data[i][3], mailing))
            #mailing_lists[users[i]] = mailing_list

    for user, mailing_list in mailing_lists:
        for committee in mailing_list:
            add_user_to_group(credentials, user, committee)

def add_all_to_committes(credentials, election_data):
    # add all users to their committees and groups
    add_officers_to_committes(credentials, election_data)
    add_members_to_committes(credentials, election_data)
