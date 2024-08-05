# backend/models.py

from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    username: str = Field(..., example="johndoe")
    password: str = Field(..., example="weak_password")
    disabled: bool = Field(..., example=False)
    full_name: Optional[str] = Field(None, example="John Doe")
    email: Optional[EmailStr] = Field(None, example="johndoe@example.com")


class People(BaseModel):
    fname: str = Field(..., example="Tooth")
    lname: str = Field(..., example="Fairy")
    timestamp: str = Field(..., example="2022-10-08 09:15:10")


class Message(BaseModel):
    message: str = Field(..., example="Default message")


class Error(Message):
    status_code: int = Field(..., example=404)
