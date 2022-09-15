from datetime import datetime
from typing import List

# from beanie import Document, Link
from pydantic import EmailStr, Field, validator, BaseModel


class User(BaseModel):

    email: EmailStr
    firstName: str
    lastName: str
    password: str
    # password: str = Field(min_length=8)


class Post(BaseModel):
    title: str
