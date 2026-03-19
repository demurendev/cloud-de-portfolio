from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'deborah',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'covid_pipeline',
    default_args=default_args,
    description='COVID data pipeline',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    # Task 1 - Extract
    extract = BashOperator(
        task_id='extract_data',
        bash_command='echo "Extracting COVID data from S3..."'
    )

    # Task 2 - Transform (REAL Glue job!!)
    transform = GlueJobOperator(
        task_id='transform_data',
        job_name='covid-etl-job',
        aws_conn_id='aws_default',
        region_name='us-east-1'
    )

    # Task 3 - Load
    load = BashOperator(
        task_id='load_to_redshift',
        bash_command='echo "Loading data to Redshift..."'
    )

    # Task 4 - Notify
    notify = BashOperator(
        task_id='notify_success',
        bash_command='echo "Pipeline completed successfully!"'
    )

    extract >> transform >> load >> notify