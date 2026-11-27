import os
from dotenv import load_dotenv
from brapi import Brapi

load_dotenv()

api_key = os.getenv("BRAPI_API_KEY")

if not api_key:
    raise ValueError("API_KEY not set")

client = Brapi(
    api_key=api_key
)

quote = client.quote.retrieve(tickers="PETR4,VALE3,ITUB4")

for stock in quote.results:
    print(f'{stock.symbol}: R${stock.regular_market_price}')
