from pydantic import BaseModel


class CreateTag(BaseModel):
    guild_id: int
    name: str
    content: str
