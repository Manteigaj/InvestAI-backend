from app.models.asset import Asset
from sqlalchemy.orm import Mapped, MappedColumn, relationship
from sqlalchemy import String, ForeignKey
from app.enums.asset_type import AssetType

class Crypto(Asset):
    __tablename__ = "crypto"

    id: Mapped[int] = MappedColumn(
        ForeignKey("asset.id"),
        primary_key=True,
    )

    blockchain: Mapped[str] = MappedColumn(
        String(30)
    )

    __mapper_args__ = {
        "polymorphic_identity": "crypto",
    }