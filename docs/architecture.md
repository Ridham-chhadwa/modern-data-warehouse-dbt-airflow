# Architecture

```text
Raw CSV data -> Python cleaning -> PostgreSQL raw tables -> dbt staging -> dbt marts -> dbt tests -> reporting tables
```

Production features: modular code, quality checks, dbt tests, Airflow orchestration, documentation.
