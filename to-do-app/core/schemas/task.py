from pydantic import BaseModel


class TaskBase(BaseModel):
    user_id: int


class TaskCreate(TaskBase):
    description: str


class TaskById(TaskBase):
    task_id: int


class TaskUpdate(TaskBase):
    task_id: int
    description: str


class TaskDelete(TaskBase):
    task_id: int
