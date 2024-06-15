from fastapi import APIRouter, Depends

from sqlalchemy import select, insert

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models.user import User
from core.schemas.user import UserRead, UserCreate

router = APIRouter(tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    users = result.all()

    return users


@router.post("", response_model=UserRead)
async def create_user(
    user_create: UserCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user

