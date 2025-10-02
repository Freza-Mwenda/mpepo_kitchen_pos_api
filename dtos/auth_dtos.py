from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime


# Pydantic Models for API
class UserBase(BaseModel):
    username: str
    email: str
    full_name: str
    role: str = "cashier"


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    user: User