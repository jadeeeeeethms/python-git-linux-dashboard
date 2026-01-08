import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))
import streamlit as st
import pandas as pd
from core.utils import (loadPrices,computeReturns,computePortfolioReturns,computeCumulativeReturns)

st.title("Portfolio Overview") #visual
tickers = ["AAPL", "MSFT", "GOOGL"]

try: #robustess fetching data
    prices = loadPrices(tickers)
    returns = computeReturns(prices)
except Exception as e:
    st.error("Data retrieval failed.Please try again later!")
    st.stop()

cum_assets = pd.DataFrame()
for t in tickers:
    cum_assets[t] = computeCumulativeReturns(returns[t])

st.subheader("Portfolio Allocation")
weights = {}
total_weight = 0
for t in tickers:
    w = st.slider(f"Weight {t}",min_value=0.0,max_value=1.0,value=1/len(tickers),step=0.01)
    weights[t] = w
    total_weight += w

if abs(total_weight-1.0) > 1e-3:
    st.error("Weights must sum to 1")
    st.stop()

weights = pd.Series(weights)
portfolio_returns = computePortfolioReturns(returns, weights)
cum_assets["Portfolio"] = computeCumulativeReturns(portfolio_returns)

st.subheader("Assets vs Portfolio – Cumulative Performance") #visual
st.line_chart(cum_assets)
st.subheader("Interpretation")
st.write("This page compares the cumulative performance of individual assets "
    "with the portfolio performance. It illustrates the diversification "
    "effect and the smoothing of returns obtained through portfolio construction.")
