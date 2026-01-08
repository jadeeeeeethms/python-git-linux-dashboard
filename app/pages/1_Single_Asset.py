import streamlit as st
import pandas as pd

from core.utils import loadPrices, computeReturns
from core.metrics import (
    max_drawdown,
    sharpe_ratio,
    annualized_return,
    annualized_volatility,
)
from core.strategies.single import buy_and_hold, momentum_vol_filter


def _controls():
    ticker = st.selectbox(
        "Select asset",
        ["AAPL", "MSFT", "GOOGL", "AMZN", "META"],
        index=0,
    )
    mode = st.selectbox("Strategy", ["Buy & Hold", "Momentum + Vol target"], index=0)

    params = {"lookback_mom": 20, "lookback_vol": 20, "vol_target": 0.20}
    if mode == "Momentum + Vol target":
        c1, c2, c3 = st.columns(3)
        with c1:
            params["lookback_mom"] = st.slider("Momentum lookback (days)", 5, 120, 20, 5)
        with c2:
            params["lookback_vol"] = st.slider("Vol lookback (days)", 5, 120, 20, 5)
        with c3:
            params["vol_target"] = st.slider("Vol target (annual)", 0.05, 0.60, 0.20, 0.01)

    show_debug = st.toggle("Debug (show raw data checks)", value=True)
    return ticker, mode, params, show_debug


def _fetch_series(ticker: str) -> tuple[pd.Series, pd.Series]:
    df = loadPrices([ticker])

    if df is None or df.empty or ticker not in df.columns:
        st.error("Yahoo (yfinance) ne renvoie aucune donnée sur cette machine pour le moment.")
        st.stop()

    px = df[ticker].dropna()
    px = px.sort_index()
    px = px[~px.index.duplicated(keep="last")]

    if px.empty:
        st.error("Série de prix vide après nettoyage.")
        st.stop()

    rets_df = computeReturns(px.to_frame())
    if rets_df is None or rets_df.empty or ticker not in rets_df.columns:
        st.error("computeReturns() n'a renvoyé aucun rendement.")
        st.stop()

    rets = rets_df[ticker].dropna()
    if rets.empty:
        st.error("Série de rendements vide après calcul.")
        st.stop()

    return px, rets


def _run_strategy(mode: str, rets: pd.Series, params: dict) -> tuple[pd.Series, pd.Series]:
    if mode == "Buy & Hold":
        strat_rets = buy_and_hold(rets)
        expo = pd.Series(1.0, index=strat_rets.index, name="Position")
        return strat_rets, expo

    strat_rets, expo = momentum_vol_filter(
        rets,
        lookback_mom=int(params["lookback_mom"]),
        lookback_vol=int(params["lookback_vol"]),
        vol_target=float(params["vol_target"]),
    )
    return strat_rets, expo.rename("Position")


def _stats(cum: pd.Series, rets: pd.Series) -> dict:
    return {
        "sharpe": sharpe_ratio(rets),
        "mdd": max_drawdown(cum),
        "ann_ret": annualized_return(cum),
        "ann_vol": annualized_volatility(rets),
        "tot_ret": float(cum.iloc[-1] - 1),
    }


def _is_nan(x) -> bool:
    return x != x


st.set_page_config(page_title="Single Asset", layout="wide")
st.title("Single Asset Dashboard")
st.caption("Data automatically refreshed every 5 minutes (local cache)")

if st.button("Refresh now"):
    st.cache_data.clear()
    st.rerun()

ticker, mode, params, show_debug = _controls()
prices, returns = _fetch_series(ticker)

st.subheader("Current price")
st.metric(label=ticker, value=round(float(prices.iloc[-1]), 2))

strat_returns, position = _run_strategy(mode, returns, params)

price_norm = (prices / prices.iloc[0]).rename("Price (normalized)")
strat_cum = (1 + strat_returns).cumprod().rename("Strategy (cum value)")

kpis = _stats(strat_cum, strat_returns)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Sharpe", f"{kpis['sharpe']:.2f}" if not _is_nan(kpis["sharpe"]) else "NA")
c2.metric("Max drawdown", f"{kpis['mdd']:.2%}" if not _is_nan(kpis["mdd"]) else "NA")
c3.metric("Ann. return", f"{kpis['ann_ret']:.2%}" if not _is_nan(kpis["ann_ret"]) else "NA")
c4.metric("Ann. vol", f"{kpis['ann_vol']:.2%}" if not _is_nan(kpis["ann_vol"]) else "NA")

st.subheader("Total return")
st.write(f"{kpis['tot_ret']:.2%}")

st.subheader("Price vs Strategy cumulative value")
st.line_chart(pd.concat([price_norm, strat_cum], axis=1).dropna())

st.subheader("Position (exposure)")
st.line_chart(position.to_frame().dropna())

if show_debug:
    st.subheader("Debug checks")
    st.write("Prices unique values:", prices.nunique())
    st.write("Returns unique values:", returns.nunique())
    st.write("Returns describe:")
    st.dataframe(returns.describe())
