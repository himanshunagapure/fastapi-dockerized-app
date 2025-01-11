from typing import List
from pydantic import BaseModel

class UserIn(BaseModel):
    """
    Schema for creating a new user.
    """
    first_name: str
    last_name: str
    age: int


class BaseResponse(BaseModel):
    """
    Schema for standard success/failure response.
    """
    success: bool


class UserListOut(BaseModel):
    """
    Schema for returning a list of users.
    """
    data: List[UserIn]
