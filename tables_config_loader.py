import configparser
import os

parser = configparser.ConfigParser()

# Construct the path relative to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.ini")

parser.read(config_file_path)


def get_table_name(
    process_name: str, tab: None
):  # tab parameter is to specify if data is coming from a specific tab from the workbook sheet
    if "ALGC" in process_name:

        if tab == "Overview":
            table = parser.get("AIP_Table_Names", f"ALGC_{tab}")
            return table

        elif tab == "Monthly":
            table = parser.get("AIP_Table_Names", f"ALGC_{tab}")
            return table

    elif process_name == "SDOH":
        table = parser.get("Acclivity_Table_Names", f"{process_name}")
        return table

    elif "PALMR" in process_name:
        table = parser.get("AIP_Table_Names", "PALMR")
        return table

    elif tab is None:

        table = parser.get("Mixed_Table_Names", process_name)
        return table
