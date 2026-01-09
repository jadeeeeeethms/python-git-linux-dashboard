import requests
import streamlit as st

@st.cache_data(ttl=300)
def fetch_quote(symbol):
    api_key = st.secrets["FINNHUB_API_KEY"]
    url = "https://finnhub.io/api/v1/quote" #temps reel
    r = requests.get(url, params={"symbol": symbol, "token": api_key}, timeout=10)
    r.raise_for_status()
    data = r.json()

    if "c" not in data:
        raise RuntimeError(f"Finnhub error: {data}")

    return data
