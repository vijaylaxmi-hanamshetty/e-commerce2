# app/crud/user.py
from app.models.user import User
from app.auth import verify_password,get_password_hash

async def create_user(username: str, password: str):
    hash_password=get_password_hash(password)
    user = await User.create(username=username, password=hash_password)
    return user

async def get_user_by_username(username: str):
    return await User.get_or_none(username=username)


async def authenticate_user(username: str, password: str):
    user = await get_user_by_username(username)
    if user and verify_password(password, user.password):
        return user
    return None
