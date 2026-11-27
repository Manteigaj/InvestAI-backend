from sqlalchemy.orm import Mapped, MappedColumn, relationship
from sqlalchemy import String, ForeignKey
from app.db.base import Base

class Portfolio(Base):
    __tablename__ = "portfolio"

    id: Mapped[int] = MappedColumn(
        primary_key=True,
    )

    name: Mapped[str] = MappedColumn(
        String(20),
        unique=True,
        nullable=False,
    )

    user_id: Mapped[int] = MappedColumn(
        ForeignKey("user.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="portfolio"
    )

    portfolio_asset: Mapped[list["PortfolioAsset"]] = relationship(
        "PortfolioAsset",
        back_populates="portfolio"
    )
