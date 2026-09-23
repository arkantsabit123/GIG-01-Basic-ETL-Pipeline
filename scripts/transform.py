# scripts/transform.py
"""
GIG 1 — BASIC ETL/ELT PIPELINE
Transform: Clean Online Retail II data

Reference: docs/blueprint.md section 4 and 12
"""

import os
import logging
from pathlib import Path
import pandas as pd

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Paths
DATA_PATH = os.getenv('DATA_PATH', '/opt/airflow/data')
STAGING_DIR = Path(DATA_PATH) / 'staging'
INPUT_FILE = STAGING_DIR / 'raw_data.csv'
OUTPUT_FILE = STAGING_DIR / 'clean_data.csv'


def transform_data():
    """Transform raw data: clean, dedupe, filter."""
    logger.info("=" * 60)
    logger.info("TRANSFORM: Starting transformation")
    logger.info("=" * 60)

    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)
    initial_rows = len(df)
    logger.info(f"Rows loaded: {initial_rows:,}")

    # 1. Drop duplicates
    df = df.drop_duplicates(subset=['Invoice', 'StockCode'])
    logger.info(f"After dedup: {len(df):,}")

    # 2. Drop nulls
    df = df.dropna(subset=['Customer ID', 'Description'])
    logger.info(f"After null drop: {len(df):,}")

    # 3. Filter negative quantity & price
    df = df[df['Quantity'] > 0]
    df = df[df['Price'] > 0]
    logger.info(f"After outlier filter: {len(df):,}")

    # 4. Rename columns to match warehouse schema
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

    # 5. Save
    df.to_csv(OUTPUT_FILE, index=False)
    logger.info(f"Saved: {OUTPUT_FILE}")
    logger.info(f"TRANSFORM: Complete — {len(df):,} rows")

    return len(df)


if __name__ == "__main__":
    transform_data()