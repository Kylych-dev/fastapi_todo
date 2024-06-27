from http import HTTPStatus
from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from db.database import get_db
from db import schemas
from secure import apikey_schema
from db.models import Token
from api.auth_handler import (
    register,
    get_users,
    create_token
)


router = APIRouter()


@router.get("/list/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/register/", response_model=schemas.LiteUser, status_code=201)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return register(db=db, user_data=user_data)


@router.post("/create_token/", response_model=schemas.Token, status_code=201)
def user_token(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return create_token(db=db, user_data=user_data)


@router.get("/self/", response_model=None)
def get_user_by_id(access_token: Annotated[str, Depends(apikey_schema)], db: Session = Depends(get_db)):
    token = db.scalar(select(Token).where(Token.access_token == access_token))
    if token:
        return {
            "id": token.user.id,
            "email": token.user.email
        }
    else:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="UNAUTHORIZED"
        )
