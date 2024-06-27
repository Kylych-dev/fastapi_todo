from fastapi import FastAPI

from apps.database import engine
from apps.account import models
from apps.to_do import models


models.core.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)




