from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

import sys

sys.path.append("/opt/airflow/Scripts")

from extract import extract_data
from transform import transform_data
from load import load_data

def extract_task():
    df = extract_data("/opt/airflow/Data/Raw/netflix_titles.csv")
    df.to_csv("/opt/airflow/Data/Processed/extracted.csv", index=False)

def transform_task():
    df = pd.read_csv("/opt/airflow/Data/Processed/extracted.csv")
    df = transform_data(df)
    df.to_csv("/opt/airflow/Data/Processed/transformed.csv", index=False)

def load_task():
    df = pd.read_csv("/opt/airflow/Data/Processed/transformed.csv")
    load_data(df)

with DAG(
    dag_id="netflix_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_task
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_task
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_task
    )

    extract >> transform >> load