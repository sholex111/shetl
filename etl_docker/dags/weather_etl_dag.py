# weather_etl_dag.py
# This DAG runs every 3 hours and executes the weather ETL pipeline.


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

def run_pipeline():
    from etl.extract_weather import extract_weather_data
    from etl.transform_weather import transform_weather_data
    from etl.upsert_to_postgres import upsert_to_postgres

    raw = extract_weather_data()
    df = transform_weather_data(raw)
    upsert_to_postgres(df)

with DAG(
    dag_id='weather_etl_every_3_hours',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='0 */3 * * *',  # every 3 hours
    catchup=False,
) as dag:
    task = PythonOperator(
        task_id='run_weather_etl',
        python_callable=run_pipeline
    )
