from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    user_id: int


class UserDelete(BaseModel):
    user_id: int
