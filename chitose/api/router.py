from fastapi import APIRouter

from .routes import ipc

api_router = APIRouter()
api_router.include_router(ipc.router, prefix="/ipc", tags=["IPC"])
