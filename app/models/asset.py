from app.db.base import Base
from app.enums.asset_type import AssetType
from decimal import Decimal
from sqlalchemy.orm import (
    Mapped,
    MappedColumn,
    relationship
)
from sqlalchemy import (
    String,
    Enum,
    UniqueConstraint,
    Numeric
)

class Asset(Base):
    __tablename__ = "asset"

    __table_args__ = (
        UniqueConstraint(
            "ticker",
            "asset_type",
            "exchange",
            name="uq_asset_ticker_exchange_type"
        ),
    )

    id: Mapped[int] = MappedColumn(
        primary_key=True,
    )

    ticker: Mapped[str] = MappedColumn(
        String(10),
        nullable=False
    )

    name: Mapped[str] = MappedColumn(
        String(20),
        nullable=False
    )

    price: Mapped[Decimal] = MappedColumn(
        Numeric(precision=10, scale=2),
        nullable=False
    )

    exchange: Mapped[str | None] = MappedColumn(
        String(50),
        nullable=True
    )

    asset_type: Mapped[AssetType] = MappedColumn(
        Enum(
            AssetType,
            name="asset_type_enum",
            values_callable=lambda enum: [
                item.value for item in enum
            ],
        ),
        nullable=False
    )

    portfolio_asset: Mapped[list["PortfolioAsset"]] = relationship(
        back_populates="asset",
    )

    __mapper_args__ = {
        "polymorphic_on": asset_type,
        "polymorphic_abstract": True,
    }