# # main.py
# from fastapi import FastAPI
# from endpoints.users import UserRouter

# app = FastAPI(title="Health Sync")

# # ✅ Include the correct router instance
# app.include_router(UserRouter, prefix="/api/user")


from fastapi import FastAPI
from endpoints.users import router as user_router
from database import init_db

app = FastAPI(title="Health Sync")
app.include_router(user_router, prefix="/api/user")

@app.on_event("startup")
async def on_startup():
    await init_db()
