from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys

# Add /opt/airflow/scripts to Python path to import run_etl properly
sys.path.append('/opt/airflow/scripts')

from flight_etl_script import run_etl

default_args = {
    'owner': 'kashar',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='flight_etl_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Daily ETL for flight data from CSV to MySQL',
    tags=['etl', 'flight', 'mysql']
) as dag:

    run_etl_task = PythonOperator(
        task_id='run_flight_etl',
        python_callable=run_etl
    )

    run_etl_task
