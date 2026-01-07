import numpy as np
import pandas as pd

TRADING_DAYS = 252


def annualized_return(cum_value: pd.Series, periods: int = TRADING_DAYS) -> float:
    if len(cum_value) < 2:
        return float("nan")
    total_years = (len(cum_value) - 1) / periods
    if total_years <= 0:
        return float("nan")
    return float(cum_value.iloc[-1] ** (1 / total_years) - 1)


def annualized_volatility(returns: pd.Series, periods: int = TRADING_DAYS) -> float:
    std = returns.std()
    if std == 0 or np.isnan(std):
        return float("nan")
    return float(std * np.sqrt(periods))


def sharpe_ratio(returns: pd.Series, rf: float = 0.0, periods: int = TRADING_DAYS) -> float:
    excess = returns - rf / periods
    vol = excess.std()
    if vol == 0 or np.isnan(vol):
        return float("nan")
    return float(excess.mean() / vol * np.sqrt(periods))


def sortino_ratio(returns: pd.Series, rf: float = 0.0, periods: int = TRADING_DAYS) -> float:
    excess = returns - rf / periods
    downside = excess[excess < 0]
    dd = downside.std()
    if dd == 0 or np.isnan(dd):
        return float("nan")
    return float(excess.mean() / dd * np.sqrt(periods))


def max_drawdown(cum_value: pd.Series) -> float:
    peak = cum_value.cummax()
    dd = (cum_value / peak) - 1.0
    return float(dd.min())
