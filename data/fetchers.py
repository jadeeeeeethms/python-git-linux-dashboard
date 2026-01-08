import yfinance as yf #recup historique via API public pr portefeuille
import pandas as pd
import streamlit as st

@st.cache_data(ttl=300)
def fetch_price(ticker):
    data = yf.download(ticker,period="1y",interval="1d",progress=False)
    if data is None or data.empty:
        raise RuntimeError(f"No data for {ticker}")
    df = data[["Close"]]
    df.columns = [ticker]
    df.index = pd.to_datetime(df.index)
    return df
