from typing import Any

from discord.ext.ipc import Client
from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import ORJSONResponse

from ..models import CreateTag, CreateTagResponseModel
from ..tasks import createTag

router = APIRouter(default_response_class=ORJSONResponse)
ipc = Client(secret_key="")


@router.get("/user/{user_id}")
async def get_user(user_id: int) -> Any:
    ipcRes = await ipc.request("get_user_data", user_id=user_id)
    return ipcRes.response


@router.post("/tags/create", status_code=202)
async def create_tag(
    request: CreateTag, background_task: BackgroundTasks
) -> CreateTagResponseModel:
    background_task.add_task(createTag, path="create_tag", data=request)
    return CreateTagResponseModel(
        status=202, message="Successfully created tag", data=request
    )
