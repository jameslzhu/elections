# @author: Anthony Ding

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import argparse

from hknlib.email.auth import get_gmail_service, get_sheets_service
from hknlib.email.message import simple_message, multipart_message, send_message
from hknlib.email.settings import SERVICE_ACCOUNT_FILE
from hknlib.indrel.input import get_companies, generate_message_body
from hknlib.indrel.settings import SENDER, USER_ID, DEBUG

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Path to the attachment file, starting from the current directory")
    args = parser.parse_args()
    gmail_service = get_gmail_service(SERVICE_ACCOUNT_FILE)
    sheets_service = get_sheets_service(SERVICE_ACCOUNT_FILE)
    if DEBUG:
        sheet_range = None
    companies = get_companies(sheets_service, sheet_range)
    for comp in companies:
        if DEBUG:
            print("Sending message to " + comp.name)
        message_text = generate_message_body(comp)
        message = None
        if args.file:
            message = multipart_message(gmail_service, comp.email, SENDER, message_text, file_path)
        else:
            message = simple_message(gmail_service, comp.email, SENDER, message_text)
        send_message(gmail_service, USER_ID, message)
        if DEBUG:
            print("Message just sent to company " + comp.name + " with following text:\n\n")
            print(message_text)

if __name__ == '__main__':
    main()