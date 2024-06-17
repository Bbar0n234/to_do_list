from sqlalchemy import UniqueConstraint

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base
from .task import Tasks


class Users(Base):
    __tablename__="users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)


Users.tasks = relationship("Tasks", order_by=Tasks.task_id, back_populates="user")
