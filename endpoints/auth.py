from fastapi import APIRouter, Depends
from models.users import Users
from typing import Annotated
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
from fastapi import HTTPException

router = APIRouter(tags=["Auth"])
SECRET_KEY = "f5a18c76ed943f4d3e92a4d9225640aa96cf40c9a34625e285bde64555240903"

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
ALGORITHM = "HS256"
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='token')

async def authenticate_user(username, password):
    user = await Users.find_one(Users.username == username)
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub': username, 'id': str(user_id)}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY,algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(status_code=401,detail="Could not validate a user.")
        return {"username":username, "id": user_id}
    except JWTError:
        raise HTTPException(status_code=401,detail="Could not validate a user.")

@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await authenticate_user(form_data.username, form_data.password)
    print("User :::::", user)
    if not user:
        return "Authentication Failed."
    token = create_access_token(user.username, user.id, timedelta(minutes=20))
    return {"access token":token, "token_type": "bearer"}
