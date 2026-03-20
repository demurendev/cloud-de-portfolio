# Stock Market Data Pipeline 📈

## Overview
An automated end-to-end data pipeline that ingests daily stock market data for 5 major tickers (AAPL, GOOGL, MSFT, AMZN, TSLA), transforms it using distributed computing, and loads it into a cloud data warehouse for analytics.

## Architecture
Alpha Vantage API → S3 (raw) → AWS Glue ETL → S3 (transformed/Parquet) → Redshift → Airflow (orchestration)

## Tech Stack
Python, Alpha Vantage API, boto3, AWS S3, AWS Glue, PySpark, Amazon Redshift Serverless, Apache Airflow, Parquet

## Key Metrics Calculated
Daily Return Percentage: percentage price change day over day
5 Day Moving Average: smoothed price trend over rolling 5 day window

## Key Findings
GOOGL was the only ticker with positive average daily returns at +0.18%
MSFT had the highest peak price at $542 but steepest decline at -0.28%

## Pipeline Flow
1. ingest.py pulls daily OHLCV data from Alpha Vantage API
2. AWS Glue PySpark job cleans data and calculates financial metrics
3. Clean Parquet files partitioned by ticker stored in S3
4. Redshift COPY command loads transformed data
5. Airflow DAG schedules entire pipeline daily at midnight