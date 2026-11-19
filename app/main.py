from fastapi import FastAPI
from app.api.routes import assets
app = FastAPI()

app.include_router(assets.router, prefix="/api", tags=["api"])

