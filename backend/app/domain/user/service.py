from app.db import SessionDep
from app.domain.user.schemas import UserRead, UserCreate
from sqlmodel import select
from app.utils.password import hash_password
from app.domain.user.models import User
from typing import Annotated
from fastapi import Depends, HTTPException


class UserService:
    def __init__(self, session: SessionDep):
        self.session = session

    def create_user(self, user_create: UserCreate) -> UserRead:
        statement = select(User).where(User.email == user_create.email)
        user = self.session.exec(statement).first()

        if user:
            raise HTTPException(status_code=400, detail="User already exists")

        hashed_password = hash_password(user_create.password)
        user = User(email=user_create.email, username=user_create.username, hashed_password=hashed_password)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return UserRead(email=user.email, username=user.username)

    def get_user(self, email: str) -> UserRead:
        statement = select(User).where(User.email == email)
        user = self.session.exec(statement).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return UserRead(email=user.email, username=user.username)

    def get_user_in_db(self, email: str) -> User:
        statement = select(User).where(User.email == email)
        user = self.session.exec(statement).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user


UserServiceDep = Annotated[UserService, Depends()]
