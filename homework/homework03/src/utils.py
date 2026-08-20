"""Reusable data-summary utilities for Stage 03."""

import pandas as pd


def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for all numeric columns."""
    return df.select_dtypes(include="number").describe()


def get_category_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sales and quantity by category."""
    return (
        df.groupby("category")
        .agg(
            sales_count=("sales", "count"),
            average_sales=("sales", "mean"),
            total_sales=("sales", "sum"),
            average_quantity=("quantity", "mean"),
            total_quantity=("quantity", "sum"),
        )
        .round(2)
    )
