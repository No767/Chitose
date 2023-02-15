from pydantic import BaseModel

from .ipc import CreateTag


class CreateTagResponseModel(BaseModel):
    status: int
    message: str
    data: CreateTag
