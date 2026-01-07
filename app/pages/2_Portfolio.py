import streamlit as st
import pandas as pd
from core.utils import (loadPrices,
    computeReturns,
    computePortfolioReturns,
    computeCumulativeReturns)

st.title("Portfolio Overview")

tickers = ["AAPL", "MSFT", "GOOGL"]

prices = loadPrices(tickers)
returns = computeReturns(prices)

cum_assets = pd.DataFrame()
for t in tickers:
    cum_assets[t] = computeCumulativeReturns(returns[t])

portfolio_returns = computePortfolioReturns(returns)
cum_assets["Portfolio"] = computeCumulativeReturns(portfolio_returns)

st.subheader("Assets vs Portfolio – Cumulative Performance")
st.line_chart(cum_assets)

st.subheader("Interpretation")
st.write("This page compares the cumulative performance of individual assets "
    "with the portfolio performance. It illustrates the diversification "
    "effect and the smoothing of returns obtained through portfolio construction.")
