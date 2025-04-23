from fastapi import APIRouter

router = APIRouter(tags=["Auth"])


@router.get("")
async def create_auth():
    return {"Authentication : Successful"}