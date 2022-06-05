import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# from sqlalchemy.util import EmailType


class Users(Base):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)


class Images(Base):
    __tablename__ = "uploaded_images"

    id = Column(Integer, primary_key=True, index=True)
    uploaded_by = Column(Integer, ForeignKey("user_account.id"))
    uploaded_at = Column(DateTime, default=datetime.datetime.utcnow)
