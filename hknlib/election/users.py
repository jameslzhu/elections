from typing import List

import random

import string

import base64
from urllib.error import HTTPError

from email.mime.text import MIMEText

from tqdm import tqdm

from hknlib.election.google_utils import build_directory_service, build_gmail_service
from hknlib.election.constants import COMPSERV_AOS, COMPSERV_OFFICERS, EMAIL_SENDER, HKN_DOMAIN


def random_pass() -> str:
    rand = random.SystemRandom()
    pool = string.ascii_letters + string.digits + string.punctuation
    while True:
        passwd = ''.join(rand.choices(pool, k=16))
        # Guarantee digits and punctuation
        if any(x in passwd for x in string.digits) and any(x in passwd for x in string.punctuation):
            return passwd


class User:
    def __init__(self, row: List[str]):
        self.first_name = row[1].strip().capitalize()
        self.last_name = row[2].strip().capitalize()
        self.username = row[3].strip()
        self.secondary_email = row[4]
        self.password = random_pass()

    @property
    def email(self):
        return f"{self.username}{HKN_DOMAIN}"

    @property
    def json(self):
        return {
            "name": {
                "familyName": self.last_name,
                "givenName": self.first_name,
            },
            "password": self.password,
            "primaryEmail": self.email,
            "emails": [
                {
                    "address": self.secondary_email,
                    "type": "work",
                    "primary": False,
                },
            ],
            "changePasswordAtNextLogin": True,
        }


def add_users(election_data: List[List[str]]):
    service = build_directory_service()
    gmail_service = build_gmail_service()

    email_template = get_email_template()

    for row in tqdm(election_data, desc="Adding users"):
        user = User(row)

        try:
            service.users().get(userKey=user.email).execute()
            continue
        except Exception:
            pass

        service.users().insert(body=user.json).execute()

        message = generate_email_message(email_template, user)
        send_message(gmail_service, "me", message)


def get_email_template() -> str:
    with open("hknlib/election/new_email_template.txt", "r") as f:
        message_text = f.read()

    return message_text


def generate_email_message(email_template: str, user: User):
    message_text = email_template.format(**{
        "first_name": user.first_name,
        "hkn_email": user.email,
        "password": user.password,
        "COMPSERV_OFFICERS": COMPSERV_OFFICERS,
        "COMPSERV_AOS": COMPSERV_AOS,
    })

    message = MIMEText(message_text)
    message['to'] = user.secondary_email
    message['from'] = EMAIL_SENDER
    message['subject'] = "[Action Required] Welcome to HKN!"

    return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('ascii')}


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
    except HTTPError:
        print('An error occurred')
