from http import HTTPStatus
from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from db.database import get_db
from db import schemas
from secure import apikey_schema
from db.models import ToDo
from .users import get_user_by_id


router = APIRouter()


@router.post("/", response_model=schemas.ToDo, status_code=201)
def create_todo(
        todo_data: schemas.ToDoCreate,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_user_by_id)):
    todo_data_dict = todo_data.dict()
    todo_data_dict['owner_id'] = current_user['id']

    new_todo = ToDo(**todo_data_dict)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.get("/", response_model=List[schemas.ToDo])
def read_todos(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_user_by_id)):
    # todos = db.query(ToDo).filter(ToDo.owner_id == current_user.id).offset(skip).limit(limit).all()
    todos = db.query(ToDo).filter(ToDo.owner_id == current_user['id']).offset(skip).limit(limit).all()
    return todos


@router.put("/{todo_id}", response_model=schemas.ToDo)
def update_todo(
        todo_id: int,
        todo_data: schemas.ToDoUpdate,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_user_by_id)):
    # todo = db.query(ToDo).filter(ToDo.id == todo_id, ToDo.owner_id == current_user.id).first()
    todo = db.query(ToDo).filter(ToDo.id == todo_id, ToDo.owner_id == current_user['id']).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ToDo not found or you don't have permission to modify it"
        )
    for key, value in todo_data.dict(exclude_unset=True).items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo


@router.delete("/{todo_id}", response_model=schemas.ToDo)
def delete_todo(
        todo_id: int,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_user_by_id)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id, ToDo.owner_id == current_user['id']).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="ToDo not found or you don't have permission to delete it"
        )
    db.delete(todo)
    db.commit()
    return todo



