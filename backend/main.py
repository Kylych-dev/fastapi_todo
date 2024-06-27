import os
import sys
sys.path.append('..')

from fastapi import FastAPI
from backend.routers import to_do as to_do_router
from backend.routers import users as users_router
from db.database import engine
from db import models

app = FastAPI()


# app.include_router(
#     router=to_do_router.router,
#     prefix='/to_do'
# )

app.include_router(
    router=users_router.router,
    prefix='/users'
)


