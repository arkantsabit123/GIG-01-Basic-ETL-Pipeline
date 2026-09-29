# streamlit-cloud/app.py
"""
GIG 1 - Basic ETL/ELT Pipeline - Standalone Dashboard

Reads CSV directly (no database connection) for Streamlit Cloud deployment.

Features:
    - 4 KPI Cards: Total Transactions, Total Revenue, Total Customers, Total Products
    - 3 Charts: Revenue by Month, Top 10 Products, Revenue by Country
    - 3 Filters: Date Range, Country, Product Category
"""

import os
from datetime import datetime
import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================
# Configuration
# ============================================

DATA_PATH = "data/sample_data.csv"

st.set_page_config(
    page_title="GIG 1 - ETL Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================
# Load Data
# ============================================

@st.cache_data(ttl=3600)
def load_data():
    """Load sample data from CSV."""
    if not os.path.exists(DATA_PATH):
        st.error(f"Data file not found: {DATA_PATH}")
        return pd.DataFrame()

    df = pd.read_csv(DATA_PATH)
    df["invoice_date"] = pd.to_datetime(df["invoice_date"])
    return df


df = load_data()

if df.empty:
    st.stop()


# ============================================
# Header
# ============================================

st.title("GIG 1 - Basic ETL/ELT Pipeline")
st.caption("Interactive dashboard for Online Retail II dataset (sample data)")


# ============================================
# Sidebar Filters
# ============================================

st.sidebar.header("Filters")
st.sidebar.markdown("---")

# Filter 1: Date Range
min_date = df["invoice_date"].min().date()
max_date = df["invoice_date"].max().date()
date_range = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

# Filter 2: Country
all_countries = sorted(df["country"].dropna().unique().tolist())
default_countries = all_countries[:10] if len(all_countries) > 10 else all_countries
selected_countries = st.sidebar.multiselect(
    "Country",
    options=all_countries,
    default=default_countries,
)

# Filter 3: Product Category (by stock_code prefix)
df["category"] = df["stock_code"].astype(str).str[:2]
all_categories = sorted(df["category"].dropna().unique().tolist())
selected_categories = st.sidebar.multiselect(
    "Product Category (Stock Code Prefix)",
    options=all_categories,
    default=all_categories,
)


# ============================================
# Apply Filters
# ============================================

filtered = df.copy()

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[
        (filtered["invoice_date"].dt.date >= start_date)
        & (filtered["invoice_date"].dt.date <= end_date)
    ]

if selected_countries:
    filtered = filtered[filtered["country"].isin(selected_countries)]

if selected_categories:
    filtered = filtered[filtered["category"].isin(selected_categories)]


# ============================================
# KPI Cards
# ============================================

st.markdown("### Key Performance Indicators")

total_transactions = len(filtered)
total_revenue = (filtered["quantity"] * filtered["unit_price"]).sum()
total_customers = filtered["customer_id"].nunique()
total_products = filtered["stock_code"].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Transactions", f"{total_transactions:,}")

with col2:
    st.metric("Total Revenue", f"GBP {total_revenue:,.2f}")

with col3:
    st.metric("Total Customers", f"{total_customers:,}")

with col4:
    st.metric("Total Products", f"{total_products:,}")

st.divider()


# ============================================
# Charts
# ============================================

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Revenue by Month")
    monthly = filtered.copy()
    monthly["month"] = monthly["invoice_date"].dt.to_period("M").astype(str)
    monthly["revenue"] = monthly["quantity"] * monthly["unit_price"]
    monthly_revenue = monthly.groupby("month")["revenue"].sum().reset_index()

    fig1 = px.line(
        monthly_revenue,
        x="month",
        y="revenue",
        markers=True,
        labels={"month": "Month", "revenue": "Revenue (GBP)"},
        color_discrete_sequence=["#1f77b4"],
    )
    fig1.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    st.subheader("Top 10 Products by Quantity")
    top_products = (
        filtered.groupby("stock_code")["quantity"].sum().nlargest(10).reset_index()
    )
    fig2 = px.bar(
        top_products,
        x="quantity",
        y="stock_code",
        orientation="h",
        labels={"quantity": "Quantity Sold", "stock_code": "Product Code"},
        color_discrete_sequence=["#ff7f0e"],
    )
    fig2.update_layout(
        height=400,
        showlegend=False,
        yaxis={"categoryorder": "total ascending"},
    )
    st.plotly_chart(fig2, use_container_width=True)


st.subheader("Revenue by Country (Top 10)")
country_revenue = filtered.copy()
country_revenue["revenue"] = country_revenue["quantity"] * country_revenue["unit_price"]
country_revenue = (
    country_revenue.groupby("country")["revenue"].sum().nlargest(10).reset_index()
)
fig3 = px.pie(
    country_revenue,
    values="revenue",
    names="country",
    hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Set3,
)
fig3.update_layout(height=450)
st.plotly_chart(fig3, use_container_width=True)


# ============================================
# Raw Data Preview
# ============================================

st.divider()
with st.expander("View Raw Data (first 100 rows)"):
    st.dataframe(filtered.head(100), use_container_width=True)
    st.caption(f"Showing first 100 rows of {len(filtered):,} filtered records")


# ============================================
# Footer
# ============================================

st.divider()
st.caption(
    f"Data Source: sample_data.csv | "
    f"Rows Loaded: {len(df):,} | "
    f"Filtered: {len(filtered):,} | "
    f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)