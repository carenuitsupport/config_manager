import configparser
import os

parser = configparser.ConfigParser()

# Construct the path relative to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.ini")

parser.read(config_file_path)


def get_closedloop_username():
    return parser.get("closedloop_credentials", "cl_username")


def get_closedloop_password():
    return parser.get("closedloop_credentials", "cl_password")


def get_closedloop_cloud_provider():
    return parser.get("closedloop_credentials", "cl_cloudProvider")
