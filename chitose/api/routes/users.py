from typing import Any

from config.pydantic_models.user import User as UserSchema
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from prisma.models import User

router = APIRouter(default_response_class=ORJSONResponse)


@router.get("/{user_id}")
async def get_user(user_id: int) -> Any:
    currUser = await User.prisma().find_first(where={"id": user_id})
    return currUser


@router.post("/create")
async def create_user(user: UserSchema) -> Any:
    await User.prisma().create(data={"email": user.email, "name": user.name})
    return user
