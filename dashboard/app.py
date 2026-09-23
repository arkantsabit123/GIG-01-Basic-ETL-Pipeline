# dashboard/app.py
"""
GIG 1 - Basic ETL/ELT Pipeline Dashboard

Placeholder dashboard for Phase 2 Docker setup.
Full implementation in Phase 6 with PostgreSQL connection.
"""

import streamlit as st
import os

st.set_page_config(
    page_title="GIG 1 - ETL Dashboard",
    page_icon="data",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main header
st.title("GIG 1 - Basic ETL/ELT Pipeline")
st.caption("Dashboard placeholder for Phase 2 - Docker and Container Setup")

# Status
st.success("Container is running successfully")

# Info
st.info("""
Dashboard will be fully implemented in Phase 6.

Planned features:
- 4 KPI Cards: Total Transactions, Total Revenue, Total Customers, Total Products
- 3 Charts: Revenue by Month, Top 10 Products, Revenue by Country
- 3 Filters: Date Range, Country, Product Category
""")

# Sidebar - environment check
st.sidebar.title("Environment")
st.sidebar.markdown("---")
st.sidebar.write(f"POSTGRES_HOST: {os.getenv('POSTGRES_HOST', 'not set')}")
st.sidebar.write(f"POSTGRES_PORT: {os.getenv('POSTGRES_PORT', 'not set')}")
st.sidebar.write(f"POSTGRES_DB: {os.getenv('POSTGRES_DB', 'not set')}")
st.sidebar.write(f"DATA_LIMIT: {os.getenv('DATA_LIMIT', 'not set')}")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("GIG 1 - Basic ETL/ELT Pipeline")
st.sidebar.caption("Version 1.0.1")