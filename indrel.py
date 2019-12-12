# @author: Anthony Ding

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

from hknlib.email.auth import get_gmail_service, get_sheets_service
from hknlib.email.message import simple_message, multipart_message, send_message
from hknlib.email.settings import SERVICE_ACCOUNT_FILE
from hknlib.indrel.input import get_companies, generate_message_body, check_if_multipart
from hknlib.indrel.settings import SENDER, USER_ID

def main():
    gmail_service = get_gmail_service(SERVICE_ACCOUNT_FILE)
    sheets_service = get_sheets_service(SERVICE_ACCOUNT_FILE)
    companies = get_companies(sheets_service, sheet_range)
    for comp in companies:
        message_text = generate_message_body(comp)
        message = None
        file_path = multipart_file_path()
        if file_path:
            message = multipart_message(gmail_service, comp, SENDER, message_text, file_path)
        else:
            message = simple_message(gmail_service, comp, SENDER, message_text)
        send_message(gmail_service, USER_ID, message)
        if DEBUG:
            print("Message just sent to company " + comp + " with following text:\n\n")
            print(message_text)
