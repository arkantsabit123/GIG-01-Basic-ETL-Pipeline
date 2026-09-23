# GIG 1 — BASIC ETL/ELT PIPELINE
# README.md

---

# Basic ETL/ELT Pipeline

## End-to-End Data Engineering Project with Apache Airflow, PostgreSQL, and Streamlit

[![Airflow](https://img.shields.io/badge/Airflow-2.7.3-blue)](https://airflow.apache.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)](https://www.postgresql.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://python.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)](https://www.docker.com/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0.3-150458)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Dataset](https://img.shields.io/badge/Dataset-Online%20Retail%20II-orange)](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
[![Verification](https://img.shields.io/badge/Verification-92%20checks-brightgreen)](docs/verification-checklist.md)
[![Screenshots](https://img.shields.io/badge/Screenshots-15-blueviolet)](screenshots/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Arkan%20Tsabit-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arkan-tsabit-0b12b9407)
[![Instagram](https://img.shields.io/badge/Instagram-@arkantsabiit-E4405F?logo=instagram&logoColor=white)](https://www.instagram.com/arkantsabiit/)

---

## Project Overview

Basic ETL/ELT Pipeline is a data engineering project that demonstrates an end-to-end ETL pipeline for the Online Retail II dataset. The pipeline extracts data from the UCI Machine Learning Repository, transforms it using Pandas, loads it into PostgreSQL, and visualizes insights through an interactive Streamlit dashboard.

This project is part of the **GIG-01** service offering — designed for SaaS startups and SMEs that need to automate data pipelines from 2-3 data sources.

### Key Highlights

- **1+ Million Rows** processed from Online Retail II dataset
- **Automated ETL Pipeline** with data cleaning, deduplication, and outlier removal
- **Interactive Dashboard** with 4 KPIs, 3 charts, and 3 filters
- **Containerized Deployment** using Docker Compose (3 services)
- **Apache Airflow Orchestration** with daily scheduling at 2 AM
- **Source Dataset** from UCI Machine Learning Repository (CC BY 4.0)
- **92 Verification Checks** across 8 phases
- **15 Screenshots** for complete documentation

### Quick Stats

| Metric | Value |
|--------|-------|
| Input Rows | 1,067,371 |
| Output Rows | ~1,000,000 (after cleaning) |
| Execution Time | 3-4 minutes |
| Dashboard KPIs | 4 |
| Charts | 3 |
| Filters | 3 |
| Screenshots | 15 |
| Verification Checks | 92 |
| Docker Services | 3 (PostgreSQL, Airflow, Streamlit) |
| Python Scripts | 3 (extract, transform, load) |
| Documentation Files | 5 (blueprint, cheatsheet, checklist, changelog, README) |

---

## Live Demo

**URL:** To be determined after implementation

The dashboard will be deployed on Streamlit Cloud with 10,000 rows of sample data for fast and responsive performance.

**Features:**
- 4 KPIs: Total Transactions, Total Revenue, Total Customers, Total Products
- 3 Charts: Revenue by Month, Top 10 Products, Revenue by Country
- 3 Filters: Date Range, Country, Product Category
- Sample data: 10,000 rows of Online Retail II

---

## Technology Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Orchestration | Apache Airflow | 2.7.3 |
| Containerization | Docker Compose | 3.8 |
| Database | PostgreSQL | 15 |
| Data Processing | Pandas | 2.0.3 |
| Dashboard | Streamlit | 1.29.0 |
| Visualization | Plotly | 5.18.0 |
| Database Adapter | SQLAlchemy | 1.4.50 |
| Excel Reader | openpyxl | 3.1.0 |
| Python | Python | 3.10+ |
| API Client | requests | 2.31.0 |
| Env Loader | python-dotenv | 1.0.0 |
| Testing | pytest | 7.4.3 |
| Linter | flake8 | 6.0.0 |

---

## System Architecture

### Architecture Diagram

![System Architecture](screenshots/architecture-diagram.png)

*Figure 1: Complete ETL pipeline architecture showing Airflow → Pandas → PostgreSQL → Streamlit flow*

Explanation of Architecture Diagram:

| Layer | Component | Function |
|-------|-----------|----------|
| Orchestration Layer | Apache Airflow | Schedules and monitors ETL tasks with retry logic |
| Processing Layer | Python + Pandas | Executes extract, transform, and load operations |
| Storage Layer | PostgreSQL 15 | Stores cleaned data in fact_trips table |
| Visualization Layer | Streamlit | Provides interactive dashboard for data exploration |
| Containerization | Docker | Ensures consistent environment across deployments |

### Data Flow Diagram

![Data Flow Diagram](screenshots/data-flow-diagram.png)

*Figure 2: Detailed data flow showing Extract to Transform to Load to Visualize pipeline*

Explanation of Data Flow Diagram:

| Step | Component | Input | Output | Description |
|------|-----------|-------|--------|-------------|
| 1 | Extract | Online Retail II (XLSX) | data/staging/raw_data.csv | Read XLSX using Pandas |
| 2 | Transform | data/staging/raw_data.csv | data/staging/clean_data.csv | Clean and engineer features |
| 3 | Load | data/staging/clean_data.csv | PostgreSQL fact_trips | Insert into database |
| 4 | Visualize | PostgreSQL fact_trips | Streamlit Dashboard | Interactive analytics |

### Entity Relationship Diagram

![ERD Diagram](screenshots/erd-diagram.png)

*Figure 3: Entity Relationship Diagram showing fact_trips table structure*

Explanation of ERD Diagram:

| Component | Description |
|-----------|-------------|
| fact_trips | Central fact table containing retail transactions |
| Primary Key | trip_id (SERIAL) auto-incrementing |
| Dimensions | invoice_no, stock_code, customer_id, country |
| Time Dimensions | invoice_date |
| Measures | quantity, unit_price |

### Dashboard Preview

![Dashboard Overview](screenshots/07-dashboard-overview.png)

*Figure 4: Full dashboard page showing 4 KPIs, 3 charts, and sidebar filters*

---

## Quick Start

```bash
# 1. Clone repository
git clone https://github.com/arkantsabit123/GIG-01-Basic-ETL-Pipeline.git
cd "GIG-01-Basic-ETL-ELT-Pipeline"

# 2. Start all containers
docker-compose up -d

# 3. Verify containers are running
docker-compose ps

# 4. Access Airflow UI
# http://localhost:8080 (admin/admin)

# 5. Access Dashboard
# http://localhost:8501

# 6. Trigger the DAG
# Airflow UI -> etl_pipeline -> Trigger DAG
```

---

## Deployment Guide

```bash
# 1. Clone repository
git clone https://github.com/arkantsabit123/GIG-01-Basic-ETL-Pipeline.git
cd "GIG-01-Basic-ETL-ELT-Pipeline"

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate          # Windows PowerShell: venv\Scripts\Activate.ps1
                                  # Windows CMD:         venv\Scripts\activate.bat

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download dataset
curl -L -o data/raw/online_retail_ii.zip "https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip"
# Windows PowerShell:
Expand-Archive -Path data/raw/online_retail_ii.zip -DestinationPath data/raw/
# Mac/Linux:
unzip data/raw/online_retail_ii.zip -d data/raw/

# 5. Start containers
docker-compose up -d

# 6. Verify containers
docker-compose ps

# 7. Access Airflow UI
# http://localhost:8080 (admin/admin)

# 8. Run ETL manually (optional)
python scripts/extract.py
python scripts/transform.py
python scripts/load.py

# 9. Launch Dashboard
# http://localhost:8501

# 10. Run verifications
python run_all_verifications.py
```

---

## Dashboard Features

### KPI Cards

| KPI | Calculation | Display Format |
|-----|-------------|----------------|
| Total Transactions | `COUNT(*)` | `{value:,}` |
| Total Revenue | `SUM(quantity * unit_price)` | `£{value:,.2f}` |
| Total Customers | `COUNT(DISTINCT customer_id)` | `{value:,}` |
| Total Products | `COUNT(DISTINCT stock_code)` | `{value:,}` |

### Charts

| Chart | Type | Description |
|-------|------|-------------|
| Revenue by Month | Line Chart | Monthly revenue trend |
| Top 10 Products | Bar Chart | Best-selling products by quantity |
| Revenue by Country | Pie Chart | Revenue distribution by country |

### Filters

| Filter | Type | Options |
|--------|------|---------|
| Date Range | Date picker | Full period (2009-2011) |
| Country | Multiselect | All countries |
| Product Category | Selectbox | All categories |

---

## Project Structure

```
GIG-01-Basic-ETL-ELT-Pipeline/
├── README.md
├── LICENSE
├── .gitignore
├── .env
├── docker-compose.yml
├── requirements.txt
├── screenshots/
│   ├── architecture-diagram.png
│   ├── data-flow-diagram.png
│   ├── erd-diagram.png
│   ├── 01-folder-structure.png
│   ├── 02-source-data.png
│   ├── 03-airflow-dag-list.png
│   ├── 04-airflow-grid-success.png
│   ├── 05-airflow-tree-success.png
│   ├── 06-postgres-data.png
│   ├── 07-dashboard-overview.png
│   ├── 08-dashboard-charts.png
│   ├── 09-dashboard-filter.png
│   ├── 10-airflow-log.png
│   ├── 11-live-demo-dashboard.png
│   └── 12-live-demo-url.png
├── diagrams/
│   ├── architecture-diagram.pdf
│   ├── architecture-diagram.xml
│   ├── data-flow-diagram.pdf
│   ├── erd-diagram.dbml
│   └── erd-diagram.drawio
├── dags/
│   └── etl_pipeline.py
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── data/
│   ├── raw/
│   │   └── online_retail_II.xlsx
│   └── staging/
│       ├── raw_data.csv
│       ├── clean_data.csv
│       └── clean_data_sample.csv
├── warehouse/
│   └── init.sql
├── dashboard/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docs/
│   ├── blueprint.md
│   ├── CHANGELOG.md
│   ├── cheatsheets.md
│   └── verification-checklist.md
├── verify-phase-1.py
├── verify-phase-2.py
├── verify-phase-3.py
├── verify-phase-4.py
├── verify-phase-5.py
├── verify-phase-6.py
├── verify-phase-7.py
├── verify-phase-8.py
└── run_all_verifications.py
```

---

## Dataset

### Online Retail II

| Property | Value |
|----------|-------|
| Source | UCI Machine Learning Repository |
| URL | https://archive.ics.uci.edu/ml/datasets/Online+Retail+II |
| Format | XLSX (43.5 MB) |
| Volume | 1,067,371 rows |
| Features | 8 |
| Time Period | 01/12/2009 – 09/12/2011 |
| License | CC BY 4.0 |
| Citation | Chen, D. (2012). Online Retail II [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D |

### Variables

| Variable | Type | Description |
|----------|------|-------------|
| InvoiceNo | Integer | Invoice number (6-digit) |
| StockCode | Integer | Product code (5-digit) |
| Description | Text | Product name |
| Quantity | Integer | Quantity per transaction |
| InvoiceDate | Timestamp | Invoice date and time |
| UnitPrice | Real | Unit price in sterling (£) |
| CustomerID | Integer | Customer number (5-digit) |
| Country | Text | Country name |

### Download

```bash
# Direct download
curl -L -o data/raw/online_retail_ii.zip "https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip"

# Extract
# Windows PowerShell:
Expand-Archive -Path data/raw/online_retail_ii.zip -DestinationPath data/raw/
# Mac/Linux:
unzip data/raw/online_retail_ii.zip -d data/raw/
```

---

## Verification System

### 8-Phase Verification

| Phase | Name | Checks |
|-------|------|--------|
| 1 | Setup & Environment | 12 |
| 2 | Docker & Container Setup | 10 |
| 3 | Airflow DAG Creation | 10 |
| 4 | Pipeline Execution | 10 |
| 5 | PostgreSQL Data Verification | 10 |
| 6 | Dashboard Verification (Local) | 15 |
| 7 | Screenshots Documentation | 15 |
| 8 | Documentation & Handover | 10 |
| **TOTAL** | **All Phases** | **92** |

```bash
# Run all verifications
python run_all_verifications.py

# Individual verification
python verify-phase-1.py
python verify-phase-2.py
# ... up to verify-phase-8.py
```

---

## Acceptance Criteria

| No | Criteria | How to Verify |
|----|----------|---------------|
| 1 | DAG runs daily without error | Check Airflow UI for 3 consecutive days |
| 2 | Data loaded into PostgreSQL | `SELECT COUNT(*) FROM fact_trips` > 0 |
| 3 | Dashboard loads without error | Open http://localhost:8501 |
| 4 | All KPIs display correctly | Visual check |
| 5 | All charts render | Visual check |
| 6 | All filters work | Test each filter |
| 7 | Documentation complete | Review docs/ folder |
| 8 | Docker Compose works | `docker-compose up -d` succeeds |

---

## Handover Checklist

| No | Item | Delivered |
|----|------|:---:|
| 1 | Source code (Git repo) | |
| 2 | Docker Compose file | |
| 3 | Database schema (init.sql) | |
| 4 | Dashboard app | |
| 5 | Documentation (README, blueprint, cheatsheet) | |
| 6 | Screenshots | |
| 7 | Training session (1 hour) | |
| 8 | Access credentials | |

---

## Support & Warranty

| Item | Detail |
|------|--------|
| Warranty Period | 14 days after handover |
| Coverage | Bug fixes only |
| Response Time | < 24 hours |
| Excluded | New features, scope changes |
| Extended Support | Available as retainer ($200/month) |

---

## Assumptions & Constraints

### Assumptions

- Client provides API keys / DB credentials
- Client has Docker installed
- Client has basic understanding of SQL
- Data volume < 500K rows/day
- Source APIs are stable and documented

### Constraints

- No real-time streaming (batch only)
- No ML/AI features
- No mobile app
- Single language (Python)
- Single database (PostgreSQL)

---

## Quick Commands

```bash
# START SERVICES
docker-compose up -d

# STATUS
docker-compose ps

# LOGS
docker-compose logs -f

# STOP SERVICES
docker-compose down

# RESET
docker-compose down -v && docker-compose up -d

# AIRFLOW UI
http://localhost:8080 (admin/admin)

# DASHBOARD
http://localhost:8501

# POSTGRES CONNECT
docker exec -it gig01-postgres psql -U admin -d warehouse

# TRIGGER DAG
docker exec -it gig01-airflow airflow dags trigger etl_pipeline

# CHECK DATA
docker exec -it gig01-postgres psql -U admin -d warehouse -c "SELECT COUNT(*) FROM fact_trips;"

# RUN SCRIPTS MANUALLY
python scripts/extract.py && python scripts/transform.py && python scripts/load.py

# RUN VERIFICATIONS
python run_all_verifications.py

# DOCKER CLEANUP
docker system prune -f
```

---

## Documentation

For complete project documentation, please refer to the `/docs/` directory:

| File | Purpose |
|------|---------|
| [blueprint.md](docs/blueprint.md) | Technical blueprint |
| [cheatsheets.md](docs/cheatsheets.md) | Quick reference commands |
| [verification-checklist.md](docs/verification-checklist.md) | Testing checklist |
| [CHANGELOG.md](docs/CHANGELOG.md) | Release history |

---

## Performance (Target)

| Metric | Value |
|--------|-------|
| Input Rows | 1,067,371 |
| Output Rows | ~1,000,000 |
| Extract Time | ~60 seconds |
| Transform Time | ~30 seconds |
| Load Time | ~120 seconds |
| **Total Time** | **~3-4 minutes** |
| PostgreSQL Size | ~100 MB |

---

## Business Value

| Metric | Before | After |
|--------|--------|-------|
| Report generation | 1-2 hours manual | 3-4 minutes automated |
| Data freshness | Daily manual | Fully automated daily |
| Human error risk | High | Eliminated |
| Decision-making latency | High | Low (instant access) |

---

## Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| Docker container not starting | Check Docker Desktop is running, verify ports are available |
| Airflow DAG not appearing | Wait 30-60 seconds, restart Airflow container |
| Task stuck in running | Clear task from UI or CLI, retry |
| Database connection refused | Wait for database to initialize (10-15 seconds) |
| No data in dashboard | Run ETL scripts or trigger DAG first |
| Port already in use | Change port in docker-compose.yml |
| XLSX read error | Install openpyxl: `pip install openpyxl` |

### Logs and Debugging

```bash
# View all container logs
docker-compose logs -f

# View specific container logs
docker-compose logs airflow -f
docker-compose logs postgres -f
docker-compose logs streamlit -f

# Check container status
docker-compose ps

# Full reset
docker-compose down -v && docker-compose up -d
```

---

## Security Considerations

### Default Credentials (Change for Production)

| Service | Username | Password |
|---------|----------|----------|
| Airflow UI | admin | admin |
| PostgreSQL | admin | admin |

### Network Ports

| Port | Service | Exposure |
|------|---------|----------|
| 8080 | Airflow UI | Localhost |
| 5432 | PostgreSQL | Localhost |
| 8501 | Dashboard | Localhost |

### Security Best Practices

1. Never expose ports to public internet in production
2. Change all default credentials before production deployment
3. Use environment variables for sensitive data
4. Implement network isolation using Docker networks
5. Regularly update Docker images for security patches

---

## Quick Links

| Resource | URL |
|----------|-----|
| **Airflow UI** | http://localhost:8080 |
| **Dashboard (Local)** | http://localhost:8501 |
| **Online Retail II Dataset** | https://archive.ics.uci.edu/ml/datasets/Online+Retail+II |
| **Airflow Docs** | https://airflow.apache.org/docs/ |
| **PostgreSQL Docs** | https://www.postgresql.org/docs/ |
| **Streamlit Docs** | https://docs.streamlit.io/ |
| **Plotly Docs** | https://plotly.com/python/ |
| **Docker Docs** | https://docs.docker.com/ |

---

## Glossary

| Term | Definition |
|------|------------|
| ETL | Extract, Transform, Load |
| DAG | Directed Acyclic Graph (Airflow workflow) |
| KPI | Key Performance Indicator |
| Data Warehouse | Central repository for analytics |
| Pipeline | Series of data processing steps |
| UCI | University of California, Irvine (dataset repository) |

---

## Pricing

### Packages

| Feature | Basic | Standard | Complete |
|:---|:---:|:---:|:---:|
| **Number of Sources** | 2 | 3 | 3+ |
| **ETL Pipeline** | Yes | Yes | Yes |
| **Data Warehouse** | Yes | Yes | Yes |
| **Dashboard** | Simple (2 KPI, 1 chart) | Full (4 KPI, 3 charts) | Full + Filters |
| **Data Quality Checks** | Basic | Standard | Advanced |
| **Automated Testing** | No | Yes | Yes |
| **Documentation** | README only | README + Blueprint | README + Blueprint + Cheatsheet |
| **Screenshots** | 4 | 8 | 15 |
| **Revisions** | 1x | 2x | 3x |
| **Support** | 7 days | 14 days | 30 days |
| **Timeline** | 3-4 days | 5-6 days | 7 days |
| **Price** | $150 | $300 | $500 |

### Add-On Services

| Add-On | Price | Description |
|:---|:---|:---|
| Extra Data Source | $100/source | Add 1 additional data source |
| Extra Dashboard Page | $150/page | Add 1 additional dashboard page |
| Extended Support | $200/month | Additional support retainer |
| Training Session | $300/session | 2-hour training session |

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- UCI Machine Learning Repository for providing the Online Retail II dataset
- Apache Airflow, PostgreSQL, Streamlit, and all open-source tools used

---

## Contact

- **Project Maintainer**: Arkan Tsabit
- **Email**: [arkantsabit025@gmail.com](mailto:arkantsabit025@gmail.com)
- **Website**: [https://arkantsabit123.github.io/](https://arkantsabit123.github.io/)
- **GitHub**: [@arkantsabit123](https://github.com/arkantsabit123)
- **LinkedIn**: [Arkan Tsabit](https://www.linkedin.com/in/arkan-tsabit-0b12b9407)
- **Instagram**: [@arkantsabiit](https://www.instagram.com/arkantsabiit/)
- **Repository**: [GIG-01-Basic-ETL-Pipeline](https://github.com/arkantsabit123/GIG-01-Basic-ETL-Pipeline)

---

*Last Updated: 2026-09-23*
*Document Version: 1.0.1*