import os
import string
from email.mime.text import MIMEText, MIMEMultipart, MIMEImage, MIMEAudio, MIMEBase
from urllib.error import HTTPError
import base64

#Returns a Message Resource with raw bytes in a urlsafe RFC 2822 encoded format.
def simple_message(message_text, receiver, sender, subject):
    message = MIMEText(message_text)
    message['to'] = receiver
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('ascii')}

#Returns a Message Resource with raw bytes in a urlsafe RFC 2822 encoded format, along with file attachment.
def multipart_message(message_text, receiver, sender, subject, file):
    message = MIMEMultipart()
    message['to'] = receiver
    message['from'] = sender
    message['subject'] = subject
    body = MIMEText(message_text)
    message.attach(body)
    content_type, encoding = mimetypes.guess_type(file)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
    #Conditions for text, image, audio, or other file attachment types
    if main_type == 'text':
        fp = open(file, 'rb')
        msg = MIMEText(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(file, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(file, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(file, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(file)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('ascii')}

#Sends the Message Resource using the given Gmail service (built with googleapiclient.discovery)
def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
    except HTTPError:
        print('An error occurred')