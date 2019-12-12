from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import random
import string
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
from urllib.error import HTTPError

EMAIL_SENDER = "hkn-ops@hkn.eecs.berkeley.edu"
#Update when running scripts every year
COMPSERV_OFFICERS = "Kevin Chen, Anthony Ding, Connie Huang, Brian Yu"
COMPSERV_AOS = "Jeffrey Kim, Matthew Signorotti, Alexander Wu, Haolin Zhu"

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
    if election_data:
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
                print('User already exists: ' + email)
            except Exception as _:
                result = service.users().insert(body=body).execute()
                message = generate_email_message(firstName, EMAIL_SENDER, row[3], secondary_email, randomPass)
                send_message(gmail_service, 'me', message)
            # print('added ' + email + ' to users')
            
    return

def generate_email_message(first_name, sender, hkn_email, receiver, password):
    #Creating and encoding email text, by Anthony Ding
    message_text = "Hi " + first_name + ",\n\n"
    message_text += "I've created an account for you at " + hkn_email + "@hkn.eecs.berkeley.edu, and added you to the lists you've requested. " 
    message_text += "Here are your account details, as well as a temporarily generated password. You will be prompted to change your password "
    message_text += "upon logging in, which you should do so promptly:\n\n"
    message_text += ("Username: " + hkn_email + "\n")
    message_text += ("Password: " + password + "\n\n")
    message_text += "This same account is used to access the HKN Wiki (prot) at https://hkn.mu/prot, and the HKN Slack at https://hkn.slack.com. " 
    message_text += "Please set your Slack display name (under Profile and Account) to your email username, so we can tag you.\n\n"
    message_text += "We've gathered a few notes about using your HKN accounts:\n\n"
    message_text += "1) These accounts are privilege given to you for HKN related business. DO NOT under any circumstances use them for any personal " 
    message_text += "or commercial business, the company you work for, for contact info in registering domains, or sending spam.\n\n"
    message_text += "2) You can create/delete/store your personal files, and of course files relating to HKN business, on your hkn.eecs.berkeley.edu "
    message_text += "Google accounts. We recommend you store files on your committee's Team Drive, where files are automatically shared with "
    message_text += "everyone on your committee (now and in the future).\n\n"
    message_text += "If you have any other questions, feel free to contact us at compserv@hkn.eecs.berkeley.edu.\n\n"
    message_text += "Best,\nCompserv\n"
    message_text += (COMPSERV_OFFICERS + "\n" + COMPSERV_AOS + "\n")
    message = MIMEText(message_text)
    message['to'] = receiver
    message['from'] = sender
    message['subject'] = "[Action Required] Welcome to HKN!"
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('ascii')}

def send_message(service, user_id, message):
    #Uses Gmail API to send message, by Anthony Ding
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
    except HTTPError:
        print('An error occurred')