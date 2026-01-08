import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))
from data.finnhub_quote import fetch_quote
import streamlit as st
from core.utils import (loadPrices,computeReturns,computePortfolioReturns,computeCumulativeReturns,computePortfolioVolatility,computePortfolioAnnualReturn,computeCorrelationMatrix)
import numpy as np

st.set_page_config(page_title="Quant B – Portfolio", layout="wide")

st.title("Multi-Asset Portfolio Dashboard") #visual
st.caption("Data automatically refreshed every 5 minutes")

if st.button("Refresh now"):
    st.cache_data.clear()
    st.rerun()

tickers = st.multiselect("Select assets",["AAPL", "MSFT", "GOOGL", "AMZN", "META"], default=["AAPL", "MSFT", "GOOGL"])

if len(tickers) < 2:
    st.warning("Please select at least 2 assets")
    st.stop()

st.subheader("Portfolio allocation")
weights = []
for ticker in tickers:
    w = st.slider(f"Weight {ticker}", 0.0, 1.0, 1/len(tickers), 0.01)
    weights.append(w)

weights = np.array(weights)
weights = weights / weights.sum()

prices = loadPrices(tickers)
returns = computeReturns(prices)

st.subheader("Current prices (Finnhub)")
cols = st.columns(len(tickers))
for col, t in zip(cols, tickers):
    try: #robustness
        q = fetch_quote(t)
        col.metric(t, f"{q['c']:.2f}", f"{q['d']:.2f}")
    except Exception:
        col.metric(t, "N/A")

portfolio_returns = computePortfolioReturns(returns, weights)
portfolio_cumulative = computeCumulativeReturns(portfolio_returns)
assets_cumulative = computeCumulativeReturns(returns)

st.subheader("Portfolio Metrics")

col1, col2 = st.columns(2)
col1.metric("Annual Return",f"{computePortfolioAnnualReturn(portfolio_returns):.2%}")
col2.metric("Volatility",f"{computePortfolioVolatility(portfolio_returns):.2%}")

st.subheader("Correlation Matrix")
st.dataframe(computeCorrelationMatrix(returns))

st.subheader("Assets vs Portfolio – Cumulative Performance")

assets_cum = (1 + returns).cumprod()
assets_cum.columns = assets_cum.columns.get_level_values(-1)
portfolio_cum = (1 + portfolio_returns).cumprod()
plot_df = assets_cum.copy()
plot_df["Portfolio"] = portfolio_cum
plot_df.columns = plot_df.columns.get_level_values(0)
st.line_chart(plot_df)


