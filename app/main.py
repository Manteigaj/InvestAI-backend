from fastapi import FastAPI
from app.api.routes import assets, auth
from app.models import User, Portfolio, PortfolioAsset, Asset, Crypto, Stock, RealStateFund
app = FastAPI()

app.include_router(assets.router, prefix="/InvestAI")

app.include_router(auth.router, prefix="/InvestAI")


