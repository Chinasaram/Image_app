from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, schema
from .main import get_db

app = FastAPI()

# SECRET_KEY = os.getenv("SECRET_KEY", "secret")
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




# # creates a new user
# @app.post("/create_user")
# def create_user(request: schema.User, db: Session = Depends(get_db)):
#     new_user = models.Users(**request.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user


# # gets a list of users
# @app.get("/get_users", response_model=List[schema.User])  # returns all users in a list
# def get_users():
#     return schema.users
