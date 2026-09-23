# watch-pipeline.py
"""
Realtime Pipeline Watcher
Refresh status setiap 10 detik
"""
import subprocess
import time
import os
from datetime import datetime

DAG_ID = "etl_pipeline"

def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True,
                            encoding='utf-8', errors='ignore')
    return result.stdout.strip()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Starting pipeline watcher... (Ctrl+C to stop)")
    try:
        while True:
            clear()
            print("=" * 70)
            print(f"  PIPELINE WATCHER — {datetime.now().strftime('%H:%M:%S')}")
            print("=" * 70)
            
            # Get DAG runs
            runs = run(['docker', 'exec', 'gig01-airflow',
                       'airflow', 'dags', 'list-runs', '--dag-id', DAG_ID])
            print("\n[DAG Runs]")
            print(runs)
            
            # Get task states for latest run
            lines = runs.splitlines()
            latest_run_id = None
            for line in lines:
                if DAG_ID in line and 'manual__' in line or 'scheduled__' in line:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 2:
                        latest_run_id = parts[1]
                        break
            
            if latest_run_id:
                print(f"\n[Tasks for {latest_run_id}]")
                tasks = run(['docker', 'exec', 'gig01-airflow',
                            'airflow', 'tasks', 'states-for-dag-run',
                            DAG_ID, latest_run_id])
                print(tasks)
            
            # Get DB row count
            db_count = run(['docker', 'exec', 'gig01-postgres',
                           'psql', '-U', 'admin', '-d', 'warehouse',
                           '-tAc', 'SELECT COUNT(*) FROM fact_trips;'])
            print(f"\n[Database: fact_trips rows] {db_count}")
            
            print("\n" + "=" * 70)
            print("  Press Ctrl+C to stop | Auto-refresh every 10s")
            print("=" * 70)
            
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nWatcher stopped.")

if __name__ == "__main__":
    main()