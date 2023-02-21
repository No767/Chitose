from discord.ext.ipc import Client

from ..models import CreateTag

ipc = Client(secret_key="test")


async def createTag(path: str, data: CreateTag) -> None:
    await ipc.request(
        path, guild_id=data.guild_id, name=data.name, content=data.content
    )
