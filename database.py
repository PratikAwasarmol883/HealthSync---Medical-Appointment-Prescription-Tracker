from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.users import Users, Appointment, Prescription, Document

async def init_db():
    try:
        client = AsyncIOMotorClient("mongodb://localhost:27017/")
        await init_beanie(
            database=client["healthsync"],
            document_models=[Users, Appointment, Prescription, Document],
        )
        print("Database initialized successfully!")
    except Exception as e:
        print(f"❌❌❌❌ Database connection failed ❌❌❌❌: {e}")

