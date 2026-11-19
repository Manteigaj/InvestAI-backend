from app.models.asset import Asset
from sqlalchemy.orm import Mapped, MappedColumn, relationship
from sqlalchemy import String, ForeignKey
from app.enums.asset_type import AssetType

class RealStateFund(Asset):

    __tablename__ = "real_state_fund"

    id: Mapped[int] = MappedColumn(
        ForeignKey("asset.id"),
        primary_key=True,
    )

    __mapper_args__ = {
        "polymorphic_identity": "real_state_fund",
    }

