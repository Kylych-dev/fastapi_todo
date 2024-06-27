from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from api.auth_handler import register, get_users

from db.database import get_db
from db import schemas, models


router = APIRouter()


@router.get("/list/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/register/", response_model=schemas.LiteUser, status_code=201)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return register(db=db, user_data=user_data)



