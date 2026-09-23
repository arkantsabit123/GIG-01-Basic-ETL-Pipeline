# scripts/extract.py
"""
GIG 1 — BASIC ETL/ELT PIPELINE
Extract: Read Online Retail II dataset from XLSX to CSV

Reference: docs/blueprint.md section 4 (Data Flow)
Input:      /opt/airflow/data/raw/online_retail_II.xlsx
Output:     /opt/airflow/data/staging/raw_data.csv
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

# Paths (inside container: /opt/airflow/data)
DATA_PATH = os.getenv('DATA_PATH', '/opt/airflow/data')
RAW_DIR = Path(DATA_PATH) / 'raw'
STAGING_DIR = Path(DATA_PATH) / 'staging'
SOURCE_FILE = RAW_DIR / 'online_retail_II.xlsx'
OUTPUT_FILE = STAGING_DIR / 'raw_data.csv'


def extract_data() -> int:
    """
    Extract data from Online Retail II XLSX to staging CSV.

    Reads all sheets from the Excel file and concatenates them.
    The Online Retail II dataset has 2 sheets:
      - Year 2009-2010
      - Year 2010-2011

    Returns:
        int: Number of rows extracted
    """
    logger.info("=" * 60)
    logger.info("EXTRACT: Starting extraction")
    logger.info("=" * 60)

    # Ensure directories exist
    STAGING_DIR.mkdir(parents=True, exist_ok=True)

    # Check source file
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Source file not found: {SOURCE_FILE}")

    file_size_mb = SOURCE_FILE.stat().st_size / (1024 * 1024)
    logger.info(f"Reading: {SOURCE_FILE} ({file_size_mb:.2f} MB)")

    # Read all sheets from Excel and concatenate
    try:
        xls = pd.ExcelFile(SOURCE_FILE)
        sheet_names = xls.sheet_names
        logger.info(f"Sheets found: {sheet_names}")

        dfs = []
        for sheet in sheet_names:
            df_sheet = pd.read_excel(xls, sheet_name=sheet)
            logger.info(f"  Sheet '{sheet}': {len(df_sheet):,} rows")
            dfs.append(df_sheet)

        df = pd.concat(dfs, ignore_index=True)
    except Exception as e:
        logger.error(f"Failed to read Excel: {e}")
        raise

    logger.info(f"Total rows extracted: {len(df):,}")
    logger.info(f"Columns: {list(df.columns)}")

    # Save to staging
    df.to_csv(OUTPUT_FILE, index=False)
    logger.info(f"Saved: {OUTPUT_FILE}")
    logger.info(f"EXTRACT: Complete — {len(df):,} rows")

    return len(df)


if __name__ == "__main__":
    extract_data()