from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys

# path
sys.path.append("/opt/airflow/etl_project")
# sys.path.append("C:/Users/Oana/Desktop/etl_project")

from extract import extract_data
from transform import transform_data
from load import load_data

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

def run_extract(**kwargs):
    record = extract_data()
    return record  # trimite catre XCom

def run_transform(**kwargs):
    record = kwargs['ti'].xcom_pull(task_ids='extract')
    df = transform_data(record)
    return df.to_json()  # trimitem DataFrame ca JSON

def run_load(**kwargs):
    df_json = kwargs['ti'].xcom_pull(task_ids='transform')
    import pandas as pd
    df = pd.read_json(df_json)
    load_data(df)

#DAG
with DAG(
    dag_id='btc_price_etl',
    default_args=default_args,
    start_date=datetime(2025, 12, 1),
    schedule_interval="*/5 * * * *",
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=run_extract
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=run_transform
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=run_load
    )

    extract_task >> transform_task >> load_task
