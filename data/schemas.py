import pandas as pd

def validate_price_df(df):
    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("Index must be a DatetimeIndex")

    if df.index.tz is None:
        raise ValueError("DatetimeIndex must be timezone-aware")

    if "price" not in df.columns:
        raise ValueError("Missing 'price' column")

    if df["price"].isna().any():
        raise ValueError("Price column contains NaN values")
