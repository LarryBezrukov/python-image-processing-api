from contextlib import asynccontextmanager
from fastapi import FastAPI
from .api.api_v1.api import api_router
from .database import engine
from . import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)
