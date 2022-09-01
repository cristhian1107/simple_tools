import imaplib
import email
from email.header import decode_header
import webbrowser
import os
from engine.settings import Settings

email_user = Settings.get_email_user()
email_password = Settings.get_email_password()
email_imap = Settings.get_email_imap()

print(email_user, email_password, email_imap)

# create an IMAP4 class with SSL.
imap = imaplib.IMAP4_SSL(host=email_imap, port=993)
# authenticate
imap.login(email_user, email_password)
print(imap.list())