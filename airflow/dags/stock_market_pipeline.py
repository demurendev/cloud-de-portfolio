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
    'stock_market_pipeline',
    default_args=default_args,
    description='Stock market data pipeline - daily ingestion and transformation',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    # Task 1 - Extract stock data from Alpha Vantage API to S3
    extract = BashOperator(
        task_id='extract_stock_data',
        bash_command='python3 /opt/airflow/dags/ingest.py'
    )

    # Task 2 - Transform with Glue ETL (clean + calculate returns + moving avg)
    transform = GlueJobOperator(
        task_id='transform_stock_data',
        job_name='stock-market-etl-job',
        aws_conn_id='aws_default',
        region_name='us-east-1'
    )

    # Task 3 - Notify success
    notify = BashOperator(
        task_id='notify_success',
        bash_command='echo "Stock market pipeline completed successfully!"'
    )

    extract >> transform >> notify