# app/routes/user.py
from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user, get_user_by_username,authenticate_user
from app.auth import create_access_token
from datetime import timedelta
router = APIRouter()

@router.post("/register", response_model=UserOut)
async def register_user(user_create: UserCreate):
    existing_user = await get_user_by_username(user_create.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = await create_user(user_create.username, user_create.password)
    return new_user

@router.post("/login")
async def login_user(user_create: UserCreate):
    user = await authenticate_user(user_create.username, user_create.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=timedelta(hours=1)
    )
    return {"access_token": access_token, "token_type": "bearer"}
