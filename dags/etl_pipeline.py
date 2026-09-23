# dags/etl_pipeline.py
"""
GIG 1 — Basic ETL/ELT Pipeline — Airflow DAG

Orchestrates the ETL pipeline for Online Retail II dataset (UCI):
1. Extract: Read XLSX from data/raw/online_retail_II.xlsx
2. Transform: Clean data, remove duplicates/nulls, filter outliers
3. Load: Insert into PostgreSQL fact_trips table

Reference: docs/blueprint.md section 9
DAG ID    : etl_pipeline
Schedule  : 0 2 * * * (daily at 2 AM)
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# ============================================
# Configuration
# ============================================
DAG_ID = 'etl_pipeline'
SCHEDULE_INTERVAL = '0 2 * * *'  # daily at 2 AM (blueprint §9)
START_DATE = datetime(2026, 1, 1)  # blueprint §9
CATCHUP = False
RETRIES = 2  # blueprint §9
RETRY_DELAY = timedelta(minutes=5)
MAX_ACTIVE_RUNS = 1

# Add scripts directory to path
sys.path.insert(0, '/opt/airflow/scripts')

# Import ETL functions
from extract import extract_data
from transform import transform_data
from load import load_data


# ============================================
# Default Arguments
# ============================================
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': START_DATE,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': RETRIES,
    'retry_delay': RETRY_DELAY,
}


# ============================================
# DAG Definition
# ============================================
dag = DAG(
    DAG_ID,
    default_args=default_args,
    description='Extract, Transform, Load Online Retail II (UCI)',
    schedule_interval=SCHEDULE_INTERVAL,
    catchup=CATCHUP,
    max_active_runs=MAX_ACTIVE_RUNS,
    tags=['etl', 'batch', 'gig-01'],
)


# ============================================
# Tasks
# ============================================
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)


# ============================================
# Task Dependencies
# ============================================
extract_task >> transform_task >> load_task