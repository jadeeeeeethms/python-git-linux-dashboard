import requests
import streamlit as st
import os

@st.cache_data(ttl=300)
def fetch_quote(symbol):
    if "FINNHUB_API_KEY" in st.secrets:
        api_key = st.secrets["FINNHUB_API_KEY"]
    #Local (env var)
    else:
        api_key = os.getenv("FINNHUB_API_KEY")

    if not api_key:
        raise RuntimeError("FINNHUB_API_KEY not found")
    url = "https://finnhub.io/api/v1/quote"
    r = requests.get(url, params={ "symbol": symbol, "token": api_key}, timeout=10)

    r.raise_for_status()
    data = r.json()
    if "c" not in data:
        raise RuntimeError(f"Finnhub error: {data}")

    return data

