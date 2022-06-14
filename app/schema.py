from datetime import datetime
from typing import Union

from pydantic import BaseModel, EmailStr, FilePath


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    full_name: str
    username: str
    email: EmailStr
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


class UserInDB(User):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class Image(BaseModel):
    image: FilePath
    uploader: UserInDB
    uploaded_at: datetime = datetime.utcnow()
