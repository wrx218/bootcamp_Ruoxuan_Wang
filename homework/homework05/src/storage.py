"""Reusable environment-driven DataFrame storage helpers."""
from pathlib import Path
import pandas as pd

def write_df(df: pd.DataFrame, path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix.lower()
    if suffix == ".csv":
        df.to_csv(path, index=False)
    elif suffix == ".parquet":
        try:
            df.to_parquet(path, index=False)
        except ImportError as exc:
            raise RuntimeError("Parquet support requires pyarrow or fastparquet. Install with: pip install pyarrow") from exc
    else:
        raise ValueError(f"Unsupported file suffix: {suffix}")
    return path

def read_df(path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Data file does not exist: {path}")
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path, parse_dates=["date"])
    if path.suffix.lower() == ".parquet":
        try:
            return pd.read_parquet(path)
        except ImportError as exc:
            raise RuntimeError("Parquet support requires pyarrow or fastparquet. Install with: pip install pyarrow") from exc
    raise ValueError(f"Unsupported file suffix: {path.suffix}")

def validate_reloads(original, csv_df, parquet_df):
    return {
        "csv_shape_matches": csv_df.shape == original.shape,
        "parquet_shape_matches": parquet_df.shape == original.shape,
        "csv_columns_match": list(csv_df.columns) == list(original.columns),
        "parquet_columns_match": list(parquet_df.columns) == list(original.columns),
        "csv_date_is_datetime": pd.api.types.is_datetime64_any_dtype(csv_df["date"]),
        "parquet_date_is_datetime": pd.api.types.is_datetime64_any_dtype(parquet_df["date"]),
        "csv_close_is_float": pd.api.types.is_float_dtype(csv_df["close"]),
        "parquet_close_is_float": pd.api.types.is_float_dtype(parquet_df["close"]),
        "csv_volume_is_integer": pd.api.types.is_integer_dtype(csv_df["volume"]),
        "parquet_volume_is_integer": pd.api.types.is_integer_dtype(parquet_df["volume"]),
    }
