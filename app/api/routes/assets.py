from fastapi import APIRouter, HTTPException
from brapi import AsyncBrapi, NotFoundError
from dotenv import load_dotenv
import os

load_dotenv()
router = APIRouter()

api_key = os.getenv("BRAPI_API_KEY")

if not api_key:
    raise ValueError("API_KEY not found")

client = AsyncBrapi(api_key=api_key)

@router.get("/api/quote/{ticker}")
async def get_quote(ticker: str):
    try:
        quote = await client.quote.retrieve(tickers=ticker)
        return {
            "ticker": quote.results[0].symbol,
            "price": quote.results[0].regular_market_price,
        }
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Ticker Not Found")