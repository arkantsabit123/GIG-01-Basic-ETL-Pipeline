# scripts/load.py
"""
GIG 1 — BASIC ETL/ELT PIPELINE
Load: Insert clean data into PostgreSQL fact_trips table

Reference: docs/blueprint.md section 4 (Data Flow)
Input:      /opt/airflow/data/staging/clean_data.csv
Output:     PostgreSQL warehouse.fact_trips
"""

import os
import logging
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Paths
DATA_PATH = os.getenv('DATA_PATH', '/opt/airflow/data')
STAGING_DIR = Path(DATA_PATH) / 'staging'
INPUT_FILE = STAGING_DIR / 'clean_data.csv'

# Database config
DB_HOST = os.getenv('POSTGRES_HOST', 'postgres')
DB_PORT = os.getenv('POSTGRES_PORT', '5432')
DB_USER = os.getenv('POSTGRES_USER', 'admin')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'admin')
DB_NAME = os.getenv('POSTGRES_DB', 'warehouse')
TABLE_NAME = 'fact_trips'


def get_engine():
    """Create SQLAlchemy engine for PostgreSQL connection."""
    url = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    return create_engine(url)


def clear_table(engine):
    """Truncate fact_trips table before loading (idempotent load)."""
    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {TABLE_NAME} RESTART IDENTITY;"))
    logger.info(f"Table '{TABLE_NAME}' truncated (idempotent load)")


def load_data() -> int:
    """
    Load clean data into PostgreSQL fact_trips table.

    Returns:
        int: Number of rows loaded
    """
    logger.info("=" * 60)
    logger.info("LOAD: Starting load to PostgreSQL")
    logger.info("=" * 60)

    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    # 1. Load clean CSV
    df = pd.read_csv(INPUT_FILE)
    logger.info(f"Rows to load: {len(df):,}")
    logger.info(f"Columns: {list(df.columns)}")

    # 2. Validate columns
    expected_columns = [
        'invoice_no', 'stock_code', 'description', 'quantity',
        'invoice_date', 'unit_price', 'customer_id', 'country'
    ]
    missing = [c for c in expected_columns if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}")

    # 3. Convert invoice_date to datetime
    df['invoice_date'] = pd.to_datetime(df['invoice_date'])

    # 4. Connect to PostgreSQL
    engine = get_engine()
    logger.info(f"Connected to {DB_HOST}:{DB_PORT}/{DB_NAME}")

    # 5. Truncate table (idempotent)
    clear_table(engine)

    # 6. Insert data in chunks
    logger.info(f"Inserting {len(df):,} rows into '{TABLE_NAME}'...")
    df.to_sql(
        TABLE_NAME,
        engine,
        if_exists='append',
        index=False,
        method='multi',
        chunksize=10000,
    )
    logger.info(f"Insert complete")

    # 7. Verify row count
    with engine.begin() as conn:
        result = conn.execute(text(f"SELECT COUNT(*) FROM {TABLE_NAME};"))
        db_count = result.scalar()

    logger.info(f"Verification: {db_count:,} rows in '{TABLE_NAME}'")
    logger.info(f"LOAD: Complete — {len(df):,} rows loaded")

    return len(df)


if __name__ == "__main__":
    load_data()