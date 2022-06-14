import os
from datetime import datetime, timedelta
from typing import List, Optional
from urllib import request

from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from . import models, schema
from .database import SessionLocal, engine

# from .schema import Image

models.Base.metadata.create_all(engine)

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()


def get_db():
    """Get the database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/upload_image", tags=["Images"])  # still working on this
def upload_image(
    image: UploadFile = File(...),
    uploaded_by: str = Form(...),
    uploaded_at: datetime = Form(datetime.utcnow()),
    db: Session = Depends(get_db),
):
    """Uploads an image to the server"""
    new_image = models.Images(Image=image.file, uploaded_by=uploaded_by, uploaded_at=uploaded_at)
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    return new_image


@app.get("/get_image/all", tags=["Images"])
def get_all_images():
    """Gets all images from the server"""
    pass


@app.put("/update_image/{image_id}", tags=["Images"])
def update_image():
    """Updates an image on the server"""
    pass


@app.delete("/delete_image/{image_id}", tags=["Images"])
def delete_image(image_id: str, Image: models.Images = Depends(models.Images)):
    """Deletes an image from the server"""
    pass


@app.get("/get_image/{image_id}", tags=["Images"])
def get_image(image_id: str, Image: models.Images = Depends(models.Images)):
    """Gets an image from the server"""
    pass


@app.post("/create_user", tags=["Users"])
def create_user(request: schema.User, db: Session = Depends(models.Users)):
    hashedPassword = pwd_context.hash(request.password)
    new_user = models.Users(
        full_name=request.full_name, username=request.username, email=request.email, password=hashedPassword
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# gets a list of users
@app.get("/get_all_users", tags=["Users"])  # returns all users in a list
def get_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@app.post("/login")
def login(request: schema.Login, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.username == request.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    if not pwd_context.verify(request.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(token: str):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schema.TokenData(username=username)
    except JWTError:
        raise credentials_exception
