from fastapi import APIRouter

router = APIRouter(tags=["Appointments"])

@router.get("")
async def get_appointment():
    return {"This is just a placeholder."}

