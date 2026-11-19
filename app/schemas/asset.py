from pydantic import BaseModel, Field


class AssetSchema(BaseModel):
    name: str = Field(..., description="The name of the asset")
    symbol: str = Field(..., description="The symbol of the asset")
    price: float = Field(..., description="The current price of the asset")

class GetAssetSchema(BaseModel):
    asset_id: int = Field(..., description="The ID of the asset")
    name: str = Field(..., description="The name of the asset")
    symbol: str = Field(..., description="The symbol of the asset")
    price: float = Field(..., description="The current price of the asset")
