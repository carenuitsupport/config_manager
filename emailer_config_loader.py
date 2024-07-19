import configparser
import os

parser = configparser.ConfigParser()

# Construct the path relative to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.ini")

parser.read(config_file_path)


def get_smtp_receiver_email() -> str:

    receiver = parser.get("smtp", "receiver_email")

    # Split the receiver string by semicolons and strip whitespace
    receiver_list = [email.strip() for email in receiver.split(";")]

    # If there's only one email address, return it as a string
    if len(receiver_list) == 1:
        return receiver_list[0]

    return receiver_list


def get_smtp_server() -> str:

    server = parser.get("smtp", "smtp_server")
    return server


def get_smtp_port() -> str:

    port = parser.get("smtp", "port")

    return port


def get_smtp_sender_email() -> str:

    sender = parser.get("smtp", "sender_email")

    return sender
