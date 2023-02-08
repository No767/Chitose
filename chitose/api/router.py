from api.routes import ipc, users
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(ipc.router, prefix="/ipc", tags=["ipc"])
