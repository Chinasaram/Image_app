import datetime
from enum import unique
from tkinter.tix import FileEntry

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# from sqlalchemy.util import EmailType


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    username = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.now)
    images = relationship("Images", back_populates="user")


class Images(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    Image = Column(String)
    uploaded_by = Column(Integer, ForeignKey("users.id"))
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("Users", back_populates="images")
