import random
import string
import httplib2

from apiclient.discovery import build

def add_users(credentials, election_data):
    #create new account for users, by Carolyn Wang, modified by Catherine Hu
    http = credentials.authorize(httplib2.Http())
    service = build('admin', 'directory_v1', http=http)
    if election_data:
        for row in election_data:
            firstName = row[1].strip().capitalize()
            lastName = row[2].strip().capitalize()
            randomPass = ''.join(random.choice(string.ascii_letters) for m in range(8)) + '1!'
            # print(randomPass)
            email = row[3] + '@hkn.eecs.berkeley.edu'
            secondary_email = row[4]
            #TODO: get rid of spaces, capitalize names, error catching
            body = {'name': {'familyName': lastName, 'givenName': firstName}, 'password': randomPass, 'primaryEmail': email, 'changePasswordAtNextLogin': True}
            try:
                existing_user = service.users().get(userKey=email).execute()
                print('User already exists: ' + email)
            except Exception as _:
                result = service.users().insert(body=body).execute()
            _ = service.users().update(body={'emails': [{'address': secondary_email, 'type': 'work', 'primary': False}]}).execute()
            # print('added ' + email + ' to users')
    return