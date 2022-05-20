import email
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT

class Settings(BaseModel):
    authjwt_secret_key: str = "cf2e086454c282ba8f21c1afef4a944c5d5dca0b92c3aaed173695d1c848ab7b"

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