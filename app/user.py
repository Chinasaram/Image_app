from fastapi import FastAPI, Depends, HTTPException
import schema
from typing import List
from fastapi_jwt_auth import AuthJWT


app = FastAPI()




# creates a new user
@app.post("/create_user")
def create_user(request: schema.User):
    new_user = {
        "full_name": request.full_name,
        "username": request.username,
        "email": request.email,
        "password": request.password
    }

    schema.users.append(new_user)

    return new_user

#gets a list of users
@app.get("/get_users", response_model=List[schema.User]) # returns all users in a list
def get_users():
    return schema.users



@app.post("/login")
def login(request: schema.Login, Authorize: AuthJWT=Depends()):
    for user in schema.users:
        if user["username"] == request.username and user["password"] == request.password:
            access_token=Authorize.create_access_token(subject=user["username"])
            return {"access_token": access_token}

        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return None