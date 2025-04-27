from beanie import Document
from datetime import date, datetime, timezone
from typing import List, Optional
from pydantic import Field, EmailStr

class Doctors(Document):
    name:str
    phone_number: str
    email: EmailStr
    hospital: str
    city: str
    highest_degree: str
    speciality: str
    years_of_experience: str
    registration_number: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))

    class Settings:
        name = "doctors"
