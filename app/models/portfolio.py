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
        ForeignKey("user.id")
    )

    user: Mapped["User"] = relationship(
        back_populates="portfolio"
    )

    portfolio_asset: Mapped[list["PortfolioAsset"]] = relationship(
        back_populates="portfolio"
    )
