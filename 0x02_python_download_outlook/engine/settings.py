import os
import string


class Settings():
    """Contains the environment variables.
    """

    @staticmethod
    def get_path() -> string:
        path = os.getenv('SAVE_PATH')
        return path

    @staticmethod
    def get_subfolder() -> string:
        subfolder = os.getenv('EMAIL_SUBFOLDER')
        return subfolder
