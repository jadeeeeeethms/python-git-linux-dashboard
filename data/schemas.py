import pandas as pd


def validate_price_df(df: pd.DataFrame) -> None:
    """
    Validate a price DataFrame.

    Conditions:
    - index must be a DatetimeIndex
    - index must be timezone-aware (UTC)
    - column 'price' must exist
    - no missing values
    """
    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("DataFrame index must be a DatetimeIndex")

    if df.index.tz is None:
        raise ValueError("DatetimeIndex must be timezone-aware (UTC)")

    if "price" not in df.columns:
        raise ValueError("DataFrame must contain a 'price' column")

    if df["price"].isna().any():
        raise ValueError("Price column contains NaN values")
