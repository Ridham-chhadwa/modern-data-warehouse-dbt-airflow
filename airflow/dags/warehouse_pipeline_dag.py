from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
PROJECT_PATH = '/path/to/modern-data-warehouse-dbt-airflow'
with DAG(dag_id='modern_data_warehouse_pipeline', start_date=datetime(2024,1,1), schedule_interval='@daily', catchup=False, tags=['data-engineering','dbt','warehouse']) as dag:
    ingest = BashOperator(task_id='ingest_clean_validate_raw_data', bash_command=f'cd {PROJECT_PATH} && python src/main.py')
    dbt_run = BashOperator(task_id='run_dbt_models', bash_command=f'cd {PROJECT_PATH}/dbt_project && dbt run')
    dbt_test = BashOperator(task_id='run_dbt_tests', bash_command=f'cd {PROJECT_PATH}/dbt_project && dbt test')
    ingest >> dbt_run >> dbt_test
