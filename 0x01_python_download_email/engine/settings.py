import email
import os
import string


class Settings():

    @staticmethod
    def get_email_user() -> string:
        email = os.getenv('EMAIL_USER')
        return email

    def get_email_password() -> string:
        email_password = os.getenv('EMAIL_PASSWORD')
        return email_password

    def get_email_imap() -> string:
        email_imap = os.getenv('EMAIL_IMAP')
        return email_imap
