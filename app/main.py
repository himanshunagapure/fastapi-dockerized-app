from typing import List
from fastapi import FastAPI
import os
import json

from app import services
from app.schema import UserIn, BaseResponse, UserListOut

app = FastAPI()

# Define the path to the data file
DATA_FILE = "app/data/users.json"

# Ensure the `data` directory and `users.json` exist
os.makedirs("app/data", exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump([], file)  # Initialize with an empty list if the file doesn't exist
        
@app.get("/")
async def index():
    """
    Index route for our application
    """
    return {"message": "Hello from FastAPI!"}


@app.post("/users", response_model=BaseResponse)
async def user_create(user: UserIn):
    """
    Add user data to json file
    """
    try:
        services.add_userdata(user.dict())
    except:
        return {"success": False}
    return {"success": True}


@app.get("/users", response_model=UserListOut)
async def get_users():
    """
    Read user data from json file
    """
    return services.read_usersdata()
