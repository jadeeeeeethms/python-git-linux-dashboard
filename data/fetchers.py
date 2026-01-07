import yfinance as yf
import pandas as pd
import streamlit as st

@st.cache_data(ttl=300) # 300s = 5 minutes
def fetch_price(ticker, frequency="1d"):
    data = yf.download(tickers=ticker,  period="1y",interval=frequency,progress=False)
    if data.empty:
        raise RuntimeError("No data returned")
    df = data[["Close"]].rename(columns={"Close": "price"})
    df.index = pd.to_datetime(df.index, utc=True)
    return df
