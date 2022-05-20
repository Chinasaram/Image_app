import email
import os
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT

class Settings(BaseModel):
    authjwt_secret_key: str = os.getenv("SECRET")

@AuthJWT.load_config
def load_config():
    return Settings()


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
                "password": "password"
            }  
        }

class Login(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "jdoe",
                "password": "password"
            }
        }
users = []