import os

from brapi import Brapi
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")

client = Brapi(api_key=API_KEY)

quote = client.quote.retrieve(tickers="PETR4")

stock = quote.results[0]

print(stock.regular_market_price)
