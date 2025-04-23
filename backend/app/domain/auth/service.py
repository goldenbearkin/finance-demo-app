from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from app.domain.user.service import UserServiceDep
from app.domain.auth.schemas import Token
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta, datetime, timezone
from typing import Union, Any
from app.utils.password import verify_password
from app.domain.user.schemas import UserRead

SECRET_KEY = "010f759b04f0bfd1116e822ef5f5f41a5d645334bdc8c3772ece71fa9642a816"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict[str, Any], expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def issue_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], user_service: UserServiceDep) -> Token:
    user = user_service.get_user_in_db(form_data.username)
    authenticated = verify_password(form_data.password, user.hashed_password)

    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data = {"sub": user.email, "username": user.username}
    access_token = create_access_token(data=data, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserRead:
    return get_current_user_from_token(token)


def get_current_user_from_token(token: str) -> UserRead:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email = payload.get("sub")
    username = payload.get("username")

    if email is None:
        raise credentials_exception

    return UserRead(email=email, username=username)
