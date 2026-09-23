# scripts/load.py
"""
GIG 1 — BASIC ETL/ELT PIPELINE
Load: Insert clean data into PostgreSQL

Reference: docs/blueprint.md section 4
"""

import os
import logging
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Paths
DATA_PATH = os.getenv('DATA_PATH', '/opt/airflow/data')
STAGING_DIR = Path(DATA_PATH) / 'staging'
INPUT_FILE = STAGING_DIR / 'clean_data.csv'

# DB Config
DB_HOST = os.getenv('POSTGRES_HOST', 'postgres')
DB_PORT = os.getenv('POSTGRES_PORT', '5432')
DB_USER = os.getenv('POSTGRES_USER', 'admin')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'admin')
DB_NAME = os.getenv('POSTGRES_DB', 'warehouse')
TABLE_NAME = 'fact_trips'


def get_engine():
    """Create SQLAlchemy engine."""
    url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(url)


def load_data():
    """Load clean data into PostgreSQL fact_trips table."""
    logger.info("=" * 60)
    logger.info("LOAD: Starting load to PostgreSQL")
    logger.info("=" * 60)

    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)
    logger.info(f"Rows to load: {len(df):,}")

    # Convert invoice_date to datetime
    df['invoice_date'] = pd.to_datetime(df['invoice_date'])

    # Create engine
    engine = get_engine()

    # Load to PostgreSQL
    df.to_sql(
        TABLE_NAME,
        engine,
        if_exists='append',
        index=False,
        method='multi',
        chunksize=10000,
    )

    logger.info(f"Loaded {len(df):,} rows into {TABLE_NAME}")
    logger.info(f"LOAD: Complete — {len(df):,} rows")

    return len(df)


if __name__ == "__main__":
    load_data()