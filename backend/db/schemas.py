from pydantic import BaseModel, EmailStr
from typing import List, Optional

from .models import ToDo


class ToDoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        orm_mode = True


class ToDoCreate(ToDoBase):
    pass


class ToDo(ToDoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


UserAuth = UserCreate


class UserResponse(UserBase):
    id: int
    is_active: bool
    to_do: List[ToDo] = []

    class Config:
        orm_mode: True


class LiteUser(UserBase):
    id: int


class User(UserBase):
    id: int
    is_active: bool
    todos: List[ToDo] = []

    class Config:
        orm_mode: True


class Token(BaseModel):
    access_token: str


class ToDoCreate(BaseModel):
    title: str
    description: str = None
    completed: bool = False
    owner_id: int


class ToDoUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None


class ToDo(BaseModel):
    title: str
    description: str = None
    completed: bool = False
    owner_id: int

    class Config:
        orm_mode = True
