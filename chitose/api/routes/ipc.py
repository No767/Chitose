from typing import Any

from discord.ext.ipc import Client
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

router = APIRouter(default_response_class=ORJSONResponse)
ipc = Client(secret_key="")


@router.get("/user/{user_id}")
async def get_user(user_id: int) -> Any:
    ipcRes = await ipc.request("get_user_data", user_id=user_id)
    return ipcRes.response
