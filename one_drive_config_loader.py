import configparser
import os

parser = configparser.ConfigParser()

# Construct the path relative to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.ini")

parser.read(config_file_path)

###PATH DIRECTORIES###


def get_onedrive_directory_cclf() -> str:

    return parser.get("onedrive_locations", "onedrive_cclf")


def get_onedrive_directory_palmr() -> str:

    return parser.get("onedrive_locations", "onedrive_palmr")


def get_onedrive_directory_algc() -> str:

    return parser.get("onedrive_locations", "onedrive_algc")


def get_onedrive_directory_sdoh() -> str:

    return parser.get("onedrive_locations", "onedrive_sdoh")


def get_onedrive_directory_ens() -> str:

    return parser.get("onedrive_locations", "onedrive_ens")


def get_onedrive_directory_acclivity() -> str:

    return parser.get("onedrive_locations", "onedrive_acclivity")


####GRAPH CLOUD API FOR ONE DRIVE CREDENTIALS######


def get_client_id():
    return parser.get("onedrive_config", "client_id")


def get_client_secret():
    return parser.get("onedrive_config", "client_secret")


def get_tenant_id():
    return parser.get("onedrive_config", "tenant_id")


def get_sharepoint_site_url():
    return parser.get("onedrive_config", "sharepoint_site_url")


def get_team_site_url():
    return parser.get("onedrive_config", "team_site_url")


def get_site_id():
    return parser.get("onedrive_config", "site_id")


def get_drive_id():
    return parser.get("onedrive_config", "drive_id")
