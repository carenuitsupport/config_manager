import configparser
from config_manager.config_environment import Environment, LOB
import os

parser = configparser.ConfigParser()

# Construct the path relative to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.ini")

parser.read(config_file_path)


def get_sql_uid() -> str:

    return parser.get("SQL_Credentials", "sql_uid")


def get_sql_pwd() -> str:

    return parser.get("SQL_Credentials", "sql_pwd")


def get_sql_driver() -> str:

    return parser.get("SQL_Credentials", "driver")


def get_sql_server() -> str:

    return parser.get("SQL_Credentials", "server")


def get_sql_database(db_environment: Environment, lob: LOB):

    database = (
        parser.get("SQL_Credentials", f"prod_database_{lob.value}")
        if db_environment == Environment.PROD
        else parser.get("SQL_Credentials", f"test_database_{lob.value}")
    )

    return database
