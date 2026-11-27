from datetime import datetime

from app.db.base import Base
from sqlalchemy.orm import Mapped, MappedColumn, relationship
from sqlalchemy import String

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = MappedColumn(
        primary_key=True,
    )
    username: Mapped[str] = MappedColumn(
        String(20),
        unique=True,
        nullable=False,
    )
    email: Mapped[str] = MappedColumn(
        String(255),
        unique=True,
        nullable=False,
    )
    password: Mapped[str] = MappedColumn(
        String(255),
        nullable=False,
    )
    portfolio: Mapped[list["Portfolio"]] = relationship(
        "Portfolio",
        back_populates="user"
    )

