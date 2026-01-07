import time
from pathlib import Path
import pandas as pd

from .fetchers import fetch_price
from .schemas import validate_price_df

CACHE_DIR = Path("data_cache")
CACHE_DIR.mkdir(exist_ok=True)

def cache_path(symbol, interval):
    filename = f"{symbol}_{interval}.csv"
    return CACHE_DIR / filename

def get_price(symbol, interval, ttl_seconds=300):
    path = cache_path(symbol, interval)

    if path.exists():
        age = time.time() - path.stat().st_mtime
        if age < ttl_seconds:
            df = pd.read_csv(path, index_col=0, parse_dates=True)
            validate_price_df(df)
            return df
    try:
        df = fetch_price(symbol, interval)
        validate_price_df(df)
        df.to_csv(path)
        return df
    except Exception:
        if path.exists():
            df = pd.read_csv(path, index_col=0, parse_dates=True)
            validate_price_df(df)
            return df
        else:
            raise RuntimeError("Unable to fetch data and no cache available")


