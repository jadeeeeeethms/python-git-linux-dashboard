import os
import requests

def fetch_quote(symbol):
    api_key = os.getenv("FINNHUB_API_KEY")

    if not api_key:
        raise RuntimeError("FINNHUB_API_KEY not found")

    url = "https://finnhub.io/api/v1/quote"
    r = requests.get(
        url,
        params={"symbol": symbol, "token": api_key},
        timeout=10
    )

    r.raise_for_status()
    data = r.json()

    if "c" not in data:
        raise RuntimeError(f"Finnhub error: {data}")

    return data
