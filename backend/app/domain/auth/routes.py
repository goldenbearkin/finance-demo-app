from fastapi import APIRouter
from app.domain.auth.schemas import Token
from typing import Annotated
from fastapi import Depends
from app.domain.auth.service import issue_token

router = APIRouter(prefix="/token", tags=["token"])


@router.post("/", response_model=Token)
async def get_token(token: Annotated[Token, Depends(issue_token)]) -> Token:
    return token
