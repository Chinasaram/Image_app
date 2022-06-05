from typing import Union
from uuid import UUID

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    full_name: str
    username: str
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "full_name": "John Doe",
                "username": "jdoe",
                "email": "johndoe@gmail.com",
                "password": "password",
            }
        }


class Login(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {"example": {"username": "jdoe", "password": "password"}}


class Image(BaseModel):
    image_id: UUID
    image: str
    uploader: str
    time_uploaded: str


users = []
