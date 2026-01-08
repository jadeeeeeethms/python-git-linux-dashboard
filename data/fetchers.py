import yfinance as yf
import pandas as pd

try:
    import streamlit as st
    cache = st.cache_data
except Exception:
    def cache(func=None, **kwargs):
        if func is None:
            return lambda f: f
        return func

@cache(ttl=300)  # 300s = 5 minutes
def fetch_price(ticker, frequency="1d"):
    data = yf.download(tickers=ticker,  period="1y",interval=frequency,progress=False)
    if data.empty:
        raise RuntimeError("No data returned")
    df = data[["Close"]].rename(columns={"Close": "price"})
    df.index = pd.to_datetime(df.index, utc=True)
    return df
