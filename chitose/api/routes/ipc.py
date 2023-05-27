from typing import Any

from discord.ext.ipc import Client
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

router = APIRouter(default_response_class=ORJSONResponse)
ipc = Client(secret_key="test")


@router.get("/user/{user_id}")
async def get_user(user_id: int) -> Any:
    """Gets the information about the currently logged in user"""
    ipcRes = await ipc.request("get_user_data", user_id=user_id)
    return ipcRes.response


# @router.post("/tags/create", status_code=202)
# async def create_tag(
#     request: CreateTag, background_task: BackgroundTasks
# ) -> CreateTagResponseModel:
#     background_task.add_task(createTag, path="create_tag", data=request)
#     return CreateTagResponseModel(
#         status=202, message="Successfully created tag", data=request
#     )


@router.get("/tags/{guild_id}/{name}/content")
async def get_tag_content(guild_id: int, name: str):
    ipcRes = await ipc.request("get_tag_content", guild_id=guild_id, tag_name=name)
    return ipcRes.response


@router.get("/tags/search")
async def get_tag(q: str, guild_id: int) -> Any:
    ipcRes = await ipc.request("get_tag", guild_id=guild_id, tag_name=q)
    return ipcRes.response


@router.get("/tags/{guild_id}/all")
async def get_tag(guild_id: int):
    ipcRes = await ipc.request("get_all_guild_tag", guild_id=guild_id)
    return ipcRes.response
