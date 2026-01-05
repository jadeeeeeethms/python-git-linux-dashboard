import time
from pathlib import Path
import pandas as pd

from .fetchers import fetch_price
from .schemas import validate_price_df

CACHE_DIR = Path("data_cache")
CACHE_DIR.mkdir(exist_ok=True)


def _cache_path(symbol: str, interval: str) -> Path:
    filename = f"{symbol}_{interval}.csv"
    return CACHE_DIR / filename


def get_price(
    symbol: str,
    interval: str,
    ttl_seconds: int = 300,
) -> pd.DataFrame:
    """
    Return price data using cache with TTL.

    Logic:
    - If cache exists and is fresh load cache
    - Else try live fetch
    - If live fetch fails fallback to cache
    """
    cache_file = _cache_path(symbol, interval)

    if cache_file.exists(): #1-Cache exists and is fresh
        age = time.time() - cache_file.stat().st_mtime
        if age < ttl_seconds:
            df = pd.read_csv(cache_file, index_col=0, parse_dates=True)
            validate_price_df(df)
            return df

    try: #2-Try live fetch
        df = fetch_price(symbol, interval)
        validate_price_df(df)
        df.to_csv(cache_file)
        return df

    except Exception as e: #3-Fallback to cache
        if cache_file.exists():
            df = pd.read_csv(cache_file, index_col=0, parse_dates=True)
            validate_price_df(df)
            return df
        else:
            raise RuntimeError(
                "Unable to fetch data and no cache available"
            ) from e
