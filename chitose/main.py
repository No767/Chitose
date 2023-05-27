from api import api_router
from config.settings import settings
from fastapi import FastAPI

app = FastAPI(
    title=settings.NAME, description=settings.DESCRIPTION, version=settings.VERSION
)

app.include_router(api_router)
