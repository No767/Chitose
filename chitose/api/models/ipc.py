from pydantic import BaseModel

class CreateTag(BaseModel):
    name: str
    content: str
