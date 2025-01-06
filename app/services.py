import os
import json
# File path for users.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "users.json")

# Ensure the data directory and file exist
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"data": []}, f)

def add_userdata(user_data: dict):
    """
    Add user data to users.json file
    """
    with open(DATA_FILE, "r+") as f:
        data = json.load(f)
        data["data"].append(user_data)
        f.seek(0)
        json.dump(data, f, indent=4)

def read_usersdata() -> dict:
    """
    Read user data from users.json file
    """
    with open(DATA_FILE, "r") as f:
        return json.load(f)
