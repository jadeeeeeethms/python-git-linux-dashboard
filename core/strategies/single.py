import pandas as pd

TRADING_DAYS = 252


def buy_and_hold(returns: pd.Series) -> pd.Series:
    return returns


def momentum_vol_filter(
    returns: pd.Series,
    lookback_mom: int = 20,
    lookback_vol: int = 20,
    vol_target: float = 0.20,
) -> tuple[pd.Series, pd.Series]:
    past = returns.rolling(lookback_mom).sum()
    signal = (past > 0).astype(float).shift(1).fillna(0.0)

    vol = returns.rolling(lookback_vol).std() * (TRADING_DAYS ** 0.5)
    vol = vol.replace(0, pd.NA)

    raw_pos = (vol_target / vol).clip(lower=0.0, upper=1.5)
    position = (signal * raw_pos).fillna(0.0)

    strat_returns = position * returns
    return strat_returns, position
