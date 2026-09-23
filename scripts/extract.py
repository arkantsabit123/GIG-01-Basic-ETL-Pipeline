# scripts/extract.py
"""
GIG 1 — BASIC ETL/ELT PIPELINE
Extract: Read Online Retail II dataset from XLSX

Reference: docs/blueprint.md section 4
"""

import os
import logging
from pathlib import Path
import pandas as pd

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Paths (inside container: /opt/airflow/data)
DATA_PATH = os.getenv('DATA_PATH', '/opt/airflow/data')
RAW_DIR = Path(DATA_PATH) / 'raw'
STAGING_DIR = Path(DATA_PATH) / 'staging'
SOURCE_FILE = RAW_DIR / 'online_retail_II.xlsx'
OUTPUT_FILE = STAGING_DIR / 'raw_data.csv'


def extract_data():
    """Extract data from Online Retail II XLSX to CSV."""
    logger.info("=" * 60)
    logger.info("EXTRACT: Starting extraction")
    logger.info("=" * 60)

    # Ensure directories exist
    STAGING_DIR.mkdir(parents=True, exist_ok=True)

    # Check source file
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Source file not found: {SOURCE_FILE}")

    logger.info(f"Reading: {SOURCE_FILE}")
    df = pd.read_excel(SOURCE_FILE)
    logger.info(f"Rows extracted: {len(df):,}")
    logger.info(f"Columns: {list(df.columns)}")

    # Save to staging
    df.to_csv(OUTPUT_FILE, index=False)
    logger.info(f"Saved: {OUTPUT_FILE}")
    logger.info(f"EXTRACT: Complete — {len(df):,} rows")

    return len(df)


if __name__ == "__main__":
    extract_data()