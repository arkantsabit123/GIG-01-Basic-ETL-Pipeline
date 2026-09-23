-- ============================================
-- GIG 1 — BASIC ETL/ELT PIPELINE
-- warehouse/init.sql
-- ============================================
-- Version   : 1.0.1
-- Reference : docs/blueprint.md section 5
-- ============================================
-- Initialize database schema for data warehouse
-- ============================================

-- Create schema if not exists
CREATE SCHEMA IF NOT EXISTS public;

-- ============================================
-- Table: fact_trips
-- ============================================
-- Central fact table for Online Retail II data
-- Reference: docs/blueprint.md section 5.2
-- ============================================

CREATE TABLE IF NOT EXISTS fact_trips (
    trip_id       SERIAL PRIMARY KEY,
    invoice_no    VARCHAR(20),
    stock_code    VARCHAR(20),
    description   VARCHAR(255),
    quantity      INTEGER,
    invoice_date  TIMESTAMP,
    unit_price    NUMERIC(10, 2),
    customer_id   VARCHAR(20),
    country       VARCHAR(50),
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- Indexes
-- ============================================
-- Reference: docs/blueprint.md section 5.3
-- ============================================

CREATE INDEX IF NOT EXISTS idx_invoice_date ON fact_trips(invoice_date);
CREATE INDEX IF NOT EXISTS idx_customer_id  ON fact_trips(customer_id);
CREATE INDEX IF NOT EXISTS idx_country      ON fact_trips(country);
CREATE INDEX IF NOT EXISTS idx_stock_code   ON fact_trips(stock_code);

-- ============================================
-- Confirmation
-- ============================================
DO $$
BEGIN
    RAISE NOTICE 'Database initialized: fact_trips table created with 4 indexes';
END $$;