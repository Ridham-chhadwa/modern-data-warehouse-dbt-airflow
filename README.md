# Modern Data Warehouse Pipeline with dbt, Airflow & Data Quality

## Overview
This project demonstrates a production-style data engineering pipeline for a retail/e-commerce business. It ingests raw customer, order, payment, refund, and product data, cleans and validates the data using Python, loads warehouse-ready tables, transforms the data using dbt, and orchestrates the workflow using an Airflow DAG.

## Business Problem
A business receives messy operational data from multiple systems. The data contains missing values, duplicates, invalid dates, invalid references, negative values, and inconsistent records. The goal is to create reliable warehouse tables for reporting and business decisions.

## Tech Stack
Python, Pandas, PostgreSQL, SQL, dbt, Airflow, Git/GitHub.

## Architecture
```text
Raw CSV/API Data -> Python ingestion -> Cleaning + validation -> PostgreSQL raw tables -> dbt staging models -> dbt marts -> dbt tests -> Analytics reporting
```

## How to Run Without Database
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```
Mac/Linux:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

## How to Run With PostgreSQL
Create `warehouse_db`, copy `.env.example` to `.env`, update credentials, set `run_pipeline(load_to_db=True)` in `src/main.py`, then run:
```bash
python src/main.py
cd dbt_project
dbt run
dbt test
```

