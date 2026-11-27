from app.models.asset import Asset
from sqlalchemy.orm import Mapped, MappedColumn, relationship
from sqlalchemy import ForeignKey, Numeric, UniqueConstraint
from app.db.base import Base
from decimal import Decimal

class PortfolioAsset(Base):
    __tablename__ = "portfolio_asset"

    __table_args__ = (
        UniqueConstraint("asset_id", "portfolio_id"),
    )

    id: Mapped[int] = MappedColumn(
        primary_key=True
    )

    asset_id: Mapped[int] = MappedColumn(
        ForeignKey("asset.id")
    )

    portfolio_id: Mapped[int] = MappedColumn(
        ForeignKey("portfolio.id")
    )

    quantity: Mapped[Decimal] = MappedColumn(
        Numeric(precision=10, scale=4),
        nullable=False
    )

    average_price: Mapped[Decimal] = MappedColumn(
        Numeric(precision=10, scale=4),
        nullable=False
    )

    asset: Mapped["Asset"] = relationship(
        "Asset",
        back_populates="portfolio_asset",
    )

    portfolio: Mapped["Portfolio"] = relationship(
        "Portfolio",
        back_populates="portfolio_asset"
    )
