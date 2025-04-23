# models/request_body.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from models.users import RoleEnum

class CreateUserRequestBody(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    role: RoleEnum
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None

class UpdateUserRequestBody(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
