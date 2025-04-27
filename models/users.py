from datetime import date, datetime, timezone
from typing import List, Optional
from beanie import Document
from pydantic import Field, EmailStr
from constants.constants import RoleEnum, StatusEnum
from passlib.hash import bcrypt


class Users(Document):
    full_name: str
    username: str
    email: EmailStr
    phone_number: str
    role: RoleEnum
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None
    hashed_password: str 
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))

    class Settings:
        name = "users"


class Appointment(Document):
    patient_id: str
    doctor_id: str
    appointment_date: datetime
    reason: str
    status: StatusEnum
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    notes: Optional[str] = None

    class Settings:
        name = "appointments"


class Prescription(Document):
    appointment_id: str
    prescribed_by: str  # Doctor ID
    patient_id: str
    medicines: List[str]  # ["Paracetamol 500mg - 2 times", ...]
    instructions: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))

    class Settings:
        name = "prescriptions"


class Document(Document):
    user_id: str
    title: str
    file_url: str
    uploaded_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    category: Optional[str] = None  # e.g., "lab report", "insurance"

    class Settings:
        name = "documents"
