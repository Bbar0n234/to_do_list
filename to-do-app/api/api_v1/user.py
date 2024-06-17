from fastapi import APIRouter, Depends

from sqlalchemy import select, insert, delete

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models.user import Users
from core.schemas.user import UserRead, UserCreate, UserDelete
from typing import List

router = APIRouter(tags=["Users"])


@router.get("", response_model=List[UserRead])
async def get_users(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Users).order_by(Users.user_id)
    result = await session.scalars(stmt)
    users = result.all()

    return users


@router.post("", response_model=UserRead)
async def create_user(
    user_create: UserCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    user = Users(**user_create.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user


@router.delete("", response_model=UserRead)
async def delete_user(
    user_delete: UserDelete,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    select_stmt = select(Users).where(Users.user_id==user_delete.user_id)

    result = await session.scalars(select_stmt)
    user = result.first()

    await session.delete(user)
    await session.commit()

    return user


