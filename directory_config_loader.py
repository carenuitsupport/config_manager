import configparser
import os

parser = configparser.ConfigParser()

# Construct the path relative to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.ini")

parser.read(config_file_path)

# DOWNLOAD DIRECTORY PATHS


def get_acclivity_download_directory():
    return parser.get("Acclivity_Locations", "download_destination")


def get_sdoh_download_directory():
    return parser.get("Acclivity_Locations", "sdoh_download_destination")


def get_ens_download_directory():
    return parser.get("Acclivity_Locations", "ens_download_destination")


def get_algc_download_directory():
    return parser.get("Acclivity_Locations", "algc_download_destination")


def get_cclf_download_directory():
    return parser.get("Acclivity_Locations", "cclf_download_destination")


def get_palmr_download_directory():
    return parser.get("Acclivity_Locations", "palmr_download_destination")


# PROCESSED DIRECTORY PATHS


def get_acclivity_processed_directory():
    return parser.get("Acclivity_Locations", "processed_destination")


def get_sdoh_processed_directory():
    return parser.get("Acclivity_Locations", "sdoh_processed_destination")


def get_ens_processed_directory():
    return parser.get("Acclivity_Locations", "ens_processed_destination")


def get_algc_processed_directory():
    return parser.get("Acclivity_Locations", "algc_processed_destination")


def get_cclf_processed_directory():
    return parser.get("Acclivity_Locations", "cclf_processed_destination")


def get_palmr_processed_directory():
    return parser.get("Acclivity_Locations", "palmr_processed_destination")
