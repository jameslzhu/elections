from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import random
import string
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
from urllib.error import HTTPError
from hknlib.election.settings import COMPSERV_AOS, COMPSERV_OFFICERS

EMAIL_SENDER = "hkn-ops@hkn.eecs.berkeley.edu"
#Update when running scripts every year

def random_pass() -> str:
    rand = random.SystemRandom()
    pool = string.ascii_letters + string.digits + string.punctuation
    while True:
        passwd = ''.join(rand.choices(pool, k=16))
        # Guarantee digits and punctuation
        if any(x in passwd for x in string.digits) and any(x in passwd for x in string.punctuation):
            return passwd

class User(object):
    def __init__(self, username, secondary_email, first_name=None, last_name=None):
        self.username = username
        self.secondary_email = secondary_email
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return "{}@hkn.eecs.berkeley.edu".format(self.username)

    @property
    def json(self):
        return {
            'name': {'familyName': self.last_name, 'givenName': self.first_name},
            'primaryEmail': self.email,
            'emails': [
                {
                    'address': self.secondary_email,
                    'type': 'work',
                    'primary': False,
                },
            ],
        }


def add_users(credentials, election_data):
    #create new account for users, by Carolyn Wang, modified by Catherine Hu
    service = build('admin', 'directory_v1', credentials=credentials)
    gmail_service = build('gmail', 'v1', credentials=credentials)

    if not election_data:
        return

    for row in election_data:
        firstName = row[1].strip().capitalize()
        lastName = row[2].strip().capitalize()
        randomPass = random_pass()
        # print(randomPass)
        email = row[3] + '@hkn.eecs.berkeley.edu'
        secondary_email = row[4]
        #TODO: get rid of spaces, capitalize names, error catching
        body = {
            'name': {'familyName': lastName, 'givenName': firstName},
            'password': randomPass,
            'primaryEmail': email,
            'emails': [
                {
                    'address': secondary_email,
                    'type': 'work',
                    'primary': False,
                },
            ],
            'changePasswordAtNextLogin': True
        }
        try:
            existing_user = service.users().get(userKey=email).execute()
            print('User already exists:', email)
        except Exception as _:
            message = generate_email_message(firstName, EMAIL_SENDER, row[3], secondary_email, randomPass)
            result = service.users().insert(body=body).execute()
            send_message(gmail_service, 'me', message)
            print('User', email, 'created')

def generate_email_message(first_name, sender, hkn_email, receiver, password):
    # Template can be found on https://hkn.mu/compserv-timeline
    #  under "Post-Midnight Meeting" and as "new_email_template.txt"
    message_text = ""
    with open('new_email_template.txt', 'r') as f:
        d = {
            'first_name': first_name,
            'hkn_email': hkn_email,
            'password': password,
            'COMPSERV_OFFICERS': COMPSERV_OFFICERS,
            'COMPSERV_AOS': COMPSERV_AOS
        }
        message_text = f.read()
        message_text = message_text.format(**d)
    message = MIMEText(message_text)
    message['to'] = receiver
    message['from'] = sender
    message['subject'] = "[Action Required] Welcome to HKN!"
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('ascii')}

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
    except HTTPError:
        print('An error occurred')
