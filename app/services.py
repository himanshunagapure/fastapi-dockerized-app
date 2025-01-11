import os
import json
from pathlib import Path

# Define the base directory and data file path
BASE_DIR = Path(__file__).resolve().parent
datafolder = os.path.join(BASE_DIR, "data")
datasource = os.path.join(datafolder, "users.json")

def check_dataset_exists():
    """
    Ensures that the data folder and JSON file exist. 
    If not, it creates them and initializes with an empty list.
    """
    try:
        if not os.path.exists(datafolder):
            os.mkdir(datafolder)
        if not os.path.exists(datasource):
            with open(datasource, "w") as f:
                json.dump({"data": []}, f)  # Initialize with an empty list
    except Exception as e:
        print(f"Error creating dataset: {e}")

def read_usersdata():
    """
    Reads user data from the JSON file. 
    Returns a dictionary containing the user data.
    """
    check_dataset_exists()
    try:
        with open(datasource, "r") as f:
            content = f.read()
            if not content.strip():
                return {"data": []}  # Return an empty list if the file is empty
            return json.loads(content)
    except json.JSONDecodeError:
        # Handle invalid JSON structure
        print("Error: JSON file is corrupted. Reinitializing.")
        with open(datasource, "w") as f:
            json.dump({"data": []}, f)
        return {"data": []}
    except Exception as e:
        print(f"Error reading data: {e}")
        return {"data": []}


def add_userdata(user: dict):
    """
    Adds a new user to the JSON file.
    """
    try:
        users = read_usersdata()  # Load current users
        with open(datasource, "w") as f:
            if "data" in users:
                users["data"].append(user)
            else:
                users["data"] = [user]
            json.dump(users, f, indent=2)
    except Exception as e:
        print(f"Error adding user data: {e}")
