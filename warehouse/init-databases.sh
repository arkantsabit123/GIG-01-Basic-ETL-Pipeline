#!/bin/bash
# ============================================
# GIG 1 — BASIC ETL/ELT PIPELINE
# warehouse/init-databases.sh
# ============================================
# Auto-create multiple databases on PostgreSQL init
# ============================================

function create_user_and_database() {
    local database=$1
    echo "  Checking database '$database'"

    # Cek apakah database sudah ada (connect ke 'postgres' database)
    DB_EXISTS=$(psql -tAc "SELECT 1 FROM pg_database WHERE datname='$database'" \
        -d postgres --username "$POSTGRES_USER")

    if [ "$DB_EXISTS" = "1" ]; then
        echo "  Database '$database' already exists, skipping"
    else
        echo "  Creating database '$database'"
        psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -d postgres <<-EOSQL
            CREATE DATABASE $database;
            GRANT ALL PRIVILEGES ON DATABASE $database TO $POSTGRES_USER;
EOSQL
        echo "  Database '$database' created"
    fi
}

if [ -n "$POSTGRES_MULTIPLE_DATABASES" ]; then
    echo "Multiple database creation requested: $POSTGRES_MULTIPLE_DATABASES"
    for db in $(echo $POSTGRES_MULTIPLE_DATABASES | tr ',' ' '); do
        create_user_and_database $db
    done
    echo "Multiple databases check complete"
fi