import uuid
from datetime import datetime
from typing import List

from fastapi import HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from backend.db.models import User, Token
from backend.db.schemas import UserCreate, UserAuth
from secure import pwd_context

from db.database import get_db



def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def register(db: Session, user_data: UserCreate):
    if db.scalar(select(User).where(User.email == user_data.email)):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    hashed_password = pwd_context.hash(user_data.password)
    user = User(email=user_data.email, hashed_password=hashed_password)
    # user.hashed_password = user_data.password.hash(user_data.password)
    db.add(user)
    db.commit()
    return {
        'id': user.id,
        'email': user.email,
    }


def create_token(db: Session, user_data: UserAuth):
    user: User = db.scalar(select(User).where(User.email == user_data.email))
    if not user:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Email not registered",
        )
    if not pwd_context.verify(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Incorrect password",
        )
    # token: Token = db.scalar(select(Token).where(Token.email == user_data.email))
    token: Token = Token(user_id=user.id, access_token=str(uuid.uuid4()))
    db.add(token)
    db.commit()
    return {
        "access_token": token.access_token
    }



