from api.routes import ipc
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(ipc.router, prefix="/ipc", tags=["IPC"])
