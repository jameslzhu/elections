from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from apiclient.discovery import build

import httplib2
import os
import random
import string

from .settings import SPREADSHEET_ID
from .cred import get_credentials


def add_user_to_group(credentials, user, groupKey):
    #add USER to a mail list GROUP
    http = credentials.authorize(httplib2.Http())
    service = build('admin', 'directory_v1', http=http)

    body = {
        'email': user + '@hkn.eecs.berkeley.edu',
        'role': 'MEMBER',
    }
    group = groupKey + '@hkn.eecs.berkeley.edu'
    response = service.members().hasMember(groupKey=group, memberKey=body.get('email')).execute()
    if response['isMember']:
        return
    return service.members().insert(groupKey=group, body=body).execute()


def add_officers_to_committes(credentials, election_data):
    user_committee = []
    if election_data:
        for i in range(0, len(election_data)):
            if len(election_data[i]) < 6:
                continue
            committee = election_data[i][5][:-1]
            user_committee.append((election_data[i][3], committee))
            #user_committee[users[i]] = committee

    for user, committee in user_committee:
        result = add_user_to_group(credentials, user, committee+'-officers')


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
