# models/request_body.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime, timezone
from constants.constants import StatusEnum
from models.users import RoleEnum

class CreateUserRequestBody(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    phone_number: str
    role: RoleEnum
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    password: str

class UpdateUserRequestBody(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None

class CreateAppointmentRequestBody(BaseModel):
    patient_id: str
    doctor_id: str
    appointment_date: datetime
    reason: str
    status: StatusEnum
    created_at: datetime = Field(alias="created_at", default_factory=lambda: datetime.now(tz=timezone.utc))
    notes: Optional[str]

class CreateDoctorsProfileRequestBody(BaseModel):
    name:str
    phone_number: str
    email: EmailStr
    hospital: str
    city: str
    highest_degree: str
    speciality: str
    years_of_experience: str
    registration_number:str

class UpdateDoctorsProfileRequestBody(BaseModel):
    name:str
    phone_number: str
    email: EmailStr
    hospital: str
    city: str
    highest_degree: str
    speciality: str
    years_of_experience: str
    registration_number:str