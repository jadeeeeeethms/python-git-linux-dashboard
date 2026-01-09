import numpy as np
import pandas as pd


def forecast_log_trend(prices: pd.Series, horizon: int = 20, alpha: float = 0.05) -> pd.DataFrame:
    s = prices.dropna().copy()
    s = s.sort_index()
    if len(s) < 30:
        raise ValueError("Not enough data to forecast (need at least ~30 points).")

    y = np.log(s.values.astype(float))
    x = np.arange(len(y), dtype=float)

    x_mean = x.mean()
    y_mean = y.mean()

    Sxx = np.sum((x - x_mean) ** 2)
    if Sxx == 0:
        raise ValueError("Degenerate time index for regression.")

    b1 = np.sum((x - x_mean) * (y - y_mean)) / Sxx
    b0 = y_mean - b1 * x_mean

    yhat_in = b0 + b1 * x
    resid = y - yhat_in

    n = len(y)
    s2 = np.sum(resid**2) / (n - 2)
    s_err = np.sqrt(s2)

    z = 1.96
    if alpha >= 0.10:
        z = 1.645

    x_future = np.arange(n, n + horizon, dtype=float)
    yhat_future = b0 + b1 * x_future

    se_mean = s_err * np.sqrt(1.0 / n + (x_future - x_mean) ** 2 / Sxx)
    se_pred = np.sqrt(se_mean**2 + s_err**2)

    lower = yhat_future - z * se_pred
    upper = yhat_future + z * se_pred

    last_date = s.index[-1]
    future_index = pd.bdate_range(last_date, periods=horizon + 1, freq="B")[1:]

    out = pd.DataFrame(
        {
            "yhat": np.exp(yhat_future),
            "lower": np.exp(lower),
            "upper": np.exp(upper),
        },
        index=future_index,
    )
    return out
