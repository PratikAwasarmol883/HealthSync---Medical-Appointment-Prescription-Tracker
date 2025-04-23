from fastapi import FastAPI
from endpoints.users import router as user_router
from endpoints.auth import router as auth_router
from endpoints.appointments import router as appointment_router
from database import init_db

app = FastAPI(title="Health Sync")
app.include_router(user_router, prefix="/api/user")
app.include_router(auth_router, prefix="/api/auth")
app.include_router(appointment_router, prefix="/api/appointment")

@app.on_event("startup")
async def on_startup():
    await init_db()
