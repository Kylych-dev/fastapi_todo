from datetime import datetime
from typing import List

from fastapi import HTTPException, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST

from backend.db.models import User
from backend.db.schemas import UserCreate
from secure import pwd_context


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





