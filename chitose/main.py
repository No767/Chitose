from api import api_router
from config.settings import settings
from fastapi import FastAPI
from prisma import Prisma

app = FastAPI(
    title=settings.NAME, description=settings.DESCRIPTION, version=settings.VERSION
)
db = Prisma(auto_register=True)

app.include_router(api_router)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
