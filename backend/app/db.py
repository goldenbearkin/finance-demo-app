from fastapi import Depends
from typing import Annotated
from sqlmodel import SQLModel, create_engine, Session
from app.domain.user.models import User
from app.utils.password import hash_password
import os

sqlite_file_name = "sqlite.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", sqlite_file_name))


def create_db_and_tables():
    if os.path.exists(db_path):
        print(f"Removing {db_path}")
        os.remove(db_path)

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        mock_users = [
            User(email="user1@test.com", username="user1", hashed_password=hash_password("testtest1")),
            User(email="user2@test.com", username="user2", hashed_password=hash_password("testtest2")),
        ]
        session.add_all(mock_users)
        session.commit()


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
