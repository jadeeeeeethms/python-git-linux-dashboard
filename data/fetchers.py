import pandas as pd
from typing import Optional


def fetch_price(
    symbol: str,
    interval: str,
    start: Optional[str] = None,
    end: Optional[str] = None,
) -> pd.DataFrame:
    """
    Fetch price data for one asset.

    Parameters
    ----------
    symbol : str
        Asset ticker (e.g. 'AAPL', 'BTC', 'EURUSD')
    interval : str
        Data frequency (e.g. '1m', '5m', '1h', '1d')
    start : Optional[str]
        Start date (ISO format), optional
    end : Optional[str]
        End date (ISO format), optional

    Returns
    -------
    pd.DataFrame
        Index : UTC datetime
        Columns : ['price']
    """
    raise NotImplementedError(
        "fetch_price is an interface and must be implemented "
        "with a specific data source (API or scraping)."
    )
