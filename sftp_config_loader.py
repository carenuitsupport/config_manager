import configparser
import os

parser = configparser.ConfigParser()

# Construct the path relative to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.ini")

parser.read(config_file_path)

# ACCLIVITY SFTP


def get_user_acclivity_sftp_credential() -> str:

    return parser.get("Acclivity_SFTP_Credentials", "sftp_username")


def get_pwd_acclivity_sftp_credential() -> str:

    return parser.get("Acclivity_SFTP_Credentials", "sftp_password")


def get_hostname_acclivity_sftp_credential() -> str:

    return parser.get("Acclivity_SFTP_Credentials", "sftp_hostname")


def get_port_acclivity_sftp_credential() -> str:

    return parser.get("Acclivity_SFTP_Credentials", "sftp_port")
