# Modern Data Warehouse Pipeline with dbt, Airflow & Data Quality

## Overview
This project demonstrates a production style data engineering pipeline for a retail/e-commerce business. It ingests raw customer, order, payment, refund, and product data, cleans and validates the data using Python, loads warehouse-ready tables, transforms the data using dbt, and orchestrates the workflow using an Airflow DAG.

## Business Problem
A business receives messy operational data from multiple systems. The data contains missing values, duplicates, invalid dates, invalid references, negative values, and inconsistent records. The goal is to create reliable warehouse tables for reporting and business decisions.

## Tech Stack
Python, Pandas, PostgreSQL, SQL, dbt, Airflow, Git/GitHub.

## Key Features

- Modular Python ETL pipeline for ingestion, cleaning, validation, and loading
- Data quality checks for duplicates, missing values, invalid references, invalid dates, and negative values
- Automated data quality report comparing raw and cleaned datasets
- PostgreSQL ready loading layer
- dbt staging and mart models for analytics ready warehouse design
- Airflow DAG included to demonstrate orchestration structure
- Clear project documentation for setup, execution, and troubleshooting

## Architecture
```text
Raw CSV/API Data -> Python ingestion -> Cleaning + validation -> PostgreSQL raw tables -> dbt staging models -> dbt marts -> dbt tests -> Analytics reporting
```

## Local Execution
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


## Data Quality Output

After running the pipeline, the project generated an automated data quality report comparing raw and cleaned datasets.

| Table | Raw Records | Clean Records | Removed | Raw Missing | Clean Missing | Raw Duplicates | Clean Duplicates |
|---|---:|---:|---:|---:|---:|---:|---:|
| customers | 6 | 4 | 2 | 1 | 0 | 1 | 0 |
| products | 5 | 4 | 1 | 0 | 0 | 0 | 0 |
| orders | 8 | 4 | 4 | 0 | 0 | 1 | 0 |
| payments | 7 | 4 | 3 | 0 | 0 | 0 | 0 |
| refunds | 2 | 1 | 1 | 0 | 0 | 0 | 0 |

This demonstrates duplicate handling, missing value treatment, referential integrity checks, invalid transaction filtering, and clean analytics ready dataset creation.


## Resume Bullet

Built a production style modern data warehouse pipeline using Python, PostgreSQL, dbt style modelling and Airflow style orchestration, including raw data ingestion, data quality validation, duplicate handling, referential integrity checks, automated quality reporting, and analytics ready outputs.
