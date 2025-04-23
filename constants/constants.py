from enum import Enum

class RoleEnum(str, Enum):
    DOCTOR = "doctor"
    PATIENT = "patient"
    ADMIN = "admin"

class StatusEnum(str, Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"