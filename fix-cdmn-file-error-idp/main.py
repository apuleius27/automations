import os
import sys
from pathlib import Path
import re

def get_venv_path():
    """Returns the path to the active virtual environment."""
    if 'CONDA_PREFIX' in os.environ:
        return os.environ['CONDA_PREFIX']
    else:
        raise EnvironmentError("No virtual environment found. Please ensure this script is run within a Conda environment.")

def create_tmp_folder(venv_path):
    """Creates a tmp folder in the virtual environment if it doesn't already exist."""
    tmp_path = Path(venv_path) / 'tmp'
    tmp_path.mkdir(exist_ok=True)
    return tmp_path

def update_api_file(venv_path, tmp_path):
    """Updates the API.py file in the cdmn package."""
    api_file_path = Path(venv_path) / 'Lib' / 'site-packages' / 'cdmn' / 'API.py'
    if not api_file_path.exists():
        raise FileNotFoundError(f"API.py not found at {api_file_path}. Please ensure the 'cdmn' package is installed correctly.")
    
    # Read the content of API.py
    with open(api_file_path, 'r') as file:
        content = file.readlines()

    # Replace the path in the file content (in a dedicated list)
    new_content = []
    replacement_path = "'" + (tmp_path / 'idp_temp.txt').as_posix() + "'"
    status_change = False
    pattern = r"'\/tmp\/idp_temp\.txt'"
    for line in content:
        # Substitute the found pattern with the replacement_path if there is a match
        new_line = re.sub(pattern, replacement_path, line)
        new_content.append(new_line)
        if new_line != line:
            status_change = True

    if not status_change:
        return status_change
    else:
        # Write the updated content back to API.py
        with open(api_file_path, 'w') as file:
            file.writelines(new_content)
        return status_change


if __name__ == "__main__":
    try:
        # Get path of the currently active virtual environment
        venv_path = get_venv_path()
        print(f"Virtual environment found at: {venv_path}")

        # Create the tmp folder if it is missing
        tmp_path = create_tmp_folder(venv_path)
        print(f"tmp directory ensured at: {tmp_path}")

        # Update the cdmn API.py file with the absolute path
        status_change = update_api_file(venv_path, tmp_path)
        if status_change:
            print("API.py has been successfully updated.")
        else:
            print("API.py already up to date or no changes needed.")
    except Exception as e:
        print(f"An error occurred: {e}")

