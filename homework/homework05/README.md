# Homework 05: Data Storage

This submission provides a reproducible storage layer for a typed IBM market-price DataFrame.

## Data Storage

- data/raw contains CSV files for readability and portability.
- data/processed contains Parquet files for type preservation and efficient analytics.
- .env defines DATA_DIR_RAW and DATA_DIR_PROCESSED; only .env.example is committed.
- src/storage.py implements suffix-based write_df and read_df, missing-directory creation, missing-file checks, and a clear missing-Parquet-engine message.
- The notebook reloads both formats and validates shapes, columns, dates, price floats, and integer volume.
