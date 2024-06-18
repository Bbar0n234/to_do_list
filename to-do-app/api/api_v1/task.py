from fastapi import APIRouter, Depends

from sqlalchemy import select, and_

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models.task import Tasks

from core.schemas.task import TaskBase, TaskCreate, TaskById, TaskUpdate, TaskDelete

from typing import List

router = APIRouter(tags=["Tasks"])


@router.get("", response_model=List[TaskUpdate])
async def get_user_tasks(
        user_id: int,
        session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Tasks).where(Tasks.user_id==user_id)
    result = await session.scalars(stmt)
    tasks = result.all()

    return tasks


@router.post("", response_model=TaskUpdate)
async def create_task(
    task_create: TaskCreate,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    task = Tasks(**task_create.model_dump())
    session.add(task)
    await session.commit()
    await session.refresh(task)

    return task


@router.put("", response_model=TaskUpdate)
async def update_task(
    task_update: TaskUpdate,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Tasks).where(and_(Tasks.user_id==task_update.user_id, Tasks.task_id==task_update.task_id))
    result = await session.scalars(stmt)
    result_task = result.first()

    result_task.description = task_update.description

    await session.commit()

    await session.refresh(result_task)

    return result_task


@router.delete("", response_model=TaskDelete)
async def delete_task(
    task_delete: TaskDelete,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Tasks).where(and_(Tasks.user_id==task_delete.user_id, Tasks.task_id==task_delete.task_id))
    result = await session.scalars(stmt)
    task = result.first()

    await session.delete(task)
    await session.commit()

    return task
