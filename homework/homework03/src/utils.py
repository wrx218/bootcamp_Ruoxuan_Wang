"""Reusable data-summary utilities for Stage 03."""

import pandas as pd


def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for numeric columns."""
    return df.select_dtypes(include="number").describe()


def get_category_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate the value column by category."""
    return (
        df.groupby("category")
        .agg(
            value_count=("value", "count"),
            average_value=("value", "mean"),
            total_value=("value", "sum"),
            minimum_value=("value", "min"),
            maximum_value=("value", "max"),
        )
        .round(2)
    )
