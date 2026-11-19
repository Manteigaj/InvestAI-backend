from decimal import Decimal
from sqlalchemy import Numeric
from app.models.asset import Asset
from sqlalchemy.orm import Mapped, MappedColumn, relationship
from sqlalchemy import String, ForeignKey
from app.enums.asset_type import AssetType

class Stock(Asset):
    __tablename__ = "stock"

    id: Mapped[int] = MappedColumn(
        ForeignKey("asset.id"),
        primary_key=True
    )

    sector: Mapped[str] = MappedColumn(
        String(30)
    )

    dividend_yield: Mapped[Decimal| None ] = MappedColumn(
        Numeric(precision=10, scale=4),
        nullable=True
    )

    __mapper_args__ = {
        "polymorphic_identity": "stock",
    }