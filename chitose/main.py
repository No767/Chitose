from api.router import api_router
from fastapi import FastAPI
from prisma import Prisma

app = FastAPI()
db = Prisma(auto_register=True)

app.include_router(api_router)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()