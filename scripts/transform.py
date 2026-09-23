# scripts/transform.py
"""
GIG 1 — BASIC ETL/ELT PIPELINE
Transform: Clean and prepare Online Retail II data

Reference: docs/blueprint.md section 4 and 12 (Data Quality Checks)
Input:      /opt/airflow/data/staging/raw_data.csv
Output:     /opt/airflow/data/staging/clean_data.csv

Data Quality Rules (blueprint §12):
  - Drop duplicates on (invoice_no, stock_code)
  - Drop nulls on customer_id and description
  - Filter quantity > 0
  - Filter unit_price >= 0.01
  - Rename columns to match warehouse schema
"""

import os
import logging
from pathlib import Path
import pandas as pd

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Paths
DATA_PATH = os.getenv('DATA_PATH', '/opt/airflow/data')
STAGING_DIR = Path(DATA_PATH) / 'staging'
INPUT_FILE = STAGING_DIR / 'raw_data.csv'
OUTPUT_FILE = STAGING_DIR / 'clean_data.csv'


def transform_data() -> int:
    """
    Transform raw data: clean, dedupe, filter, rename.

    Steps (blueprint §12):
      1. Load raw CSV
      2. Drop duplicates on (Invoice, StockCode)
      3. Drop nulls on Customer ID and Description
      4. Filter quantity > 0
      5. Filter price >= 0.01
      6. Rename columns to warehouse schema
      7. Save to clean_data.csv

    Returns:
        int: Number of rows after transformation
    """
    logger.info("=" * 60)
    logger.info("TRANSFORM: Starting transformation")
    logger.info("=" * 60)

    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)
    initial_rows = len(df)
    logger.info(f"Rows loaded: {initial_rows:,}")
    logger.info(f"Columns: {list(df.columns)}")

    # 1. Drop duplicates on (Invoice, StockCode)
    df = df.drop_duplicates(subset=['Invoice', 'StockCode'])
    logger.info(f"After dedup: {len(df):,} (removed {initial_rows - len(df):,})")

    # 2. Drop nulls on Customer ID and Description
    before_nulls = len(df)
    df = df.dropna(subset=['Customer ID', 'Description'])
    logger.info(f"After null drop: {len(df):,} (removed {before_nulls - len(df):,})")

    # 3. Filter quantity > 0
    before_qty = len(df)
    df = df[df['Quantity'] > 0]
    logger.info(f"After quantity filter (>0): {len(df):,} (removed {before_qty - len(df):,})")

    # 4. Filter price >= 0.01
    before_price = len(df)
    df = df[df['Price'] >= 0.01]
    logger.info(f"After price filter (>=0.01): {len(df):,} (removed {before_price - len(df):,})")

    # 5. Rename columns to match warehouse schema (blueprint §5.2)
    df = df.rename(columns={
        'Invoice': 'invoice_no',
        'StockCode': 'stock_code',
        'Description': 'description',
        'Quantity': 'quantity',
        'InvoiceDate': 'invoice_date',
        'Price': 'unit_price',
        'Customer ID': 'customer_id',
        'Country': 'country',
    })

    # 6. Convert data types
    df['invoice_date'] = pd.to_datetime(df['invoice_date'])
    df['quantity'] = df['quantity'].astype(int)
    df['unit_price'] = df['unit_price'].astype(float)
    df['invoice_no'] = df['invoice_no'].astype(str)
    df['stock_code'] = df['stock_code'].astype(str)
    df['customer_id'] = df['customer_id'].astype(str)

    # 7. Save
    df.to_csv(OUTPUT_FILE, index=False)
    logger.info(f"Saved: {OUTPUT_FILE}")
    logger.info(f"TRANSFORM: Complete — {len(df):,} rows")

    return len(df)


if __name__ == "__main__":
    transform_data()