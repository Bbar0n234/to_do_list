from sqlalchemy import UniqueConstraint, ForeignKey

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base


class Tasks(Base):
    __tablename__="tasks"
    task_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    description: Mapped[str] = mapped_column()

    user = relationship("Users", back_populates="tasks")

