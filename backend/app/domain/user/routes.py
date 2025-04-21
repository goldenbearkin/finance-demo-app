from typing import Annotated
from fastapi import APIRouter, Depends
from app.domain.user.service import UserServiceDep
from app.domain.user.schemas import UserCreate, UserRead
from fastapi.security import OAuth2PasswordBearer
from app.domain.auth.service import get_current_user
from app.domain.user.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=UserRead)
async def register(user_create: UserCreate, user_service: UserServiceDep):
    return user_service.create_user(user_create)


@router.get("/me", response_model=UserRead)
async def get_me(user: Annotated[User, Depends(get_current_user)], user_service: UserServiceDep):
    return user_service.get_user(user.email)
