# COVID-19 Data Pipeline 🏥

## Overview
An event driven data pipeline that ingests, transforms and analyzes COVID-19 case data across US states. Built to demonstrate end to end data engineering on AWS including automated triggering, ETL transformation and serverless querying.

## Architecture
S3 (raw CSV) → Lambda (event trigger) → AWS Glue ETL → S3 (Parquet) → Glue Crawler → Athena → Redshift (star schema)

## Tech Stack
Python, AWS S3, AWS Lambda, AWS Glue, PySpark, Amazon Athena, Amazon Redshift Serverless, Apache Airflow, Parquet

## Data Model
Star schema with three tables:
fact_covid contains case_id, state_id, date_id, cases, new_cases, deaths, new_deaths
dim_state contains state_id and state_name for all 56 US states and territories
dim_date contains date_id, date, month, year, quarter for 1158 unique dates

## Key Findings
California had the highest total cases at 12.1 million in 2021
Discovered that summing cumulative case columns inflates numbers incorrectly, MAX gives accurate totals
Negative death and case values identified as data quality issues and removed during transformation

## Pipeline Flow
1. Raw COVID CSV uploaded to S3 triggers Lambda function automatically
2. Lambda logs file details to CloudWatch and initiates pipeline
3. AWS Glue ETL job cleans nulls, removes negative values, converts CSV to Parquet
4. Glue Crawler catalogs transformed data in Glue Data Catalog
5. Athena enables serverless SQL queries directly on S3 Parquet files
6. Clean data loaded into Redshift star schema for repeated analytical queries
7. Airflow DAG orchestrates and schedules the full pipeline

## Files
- `covid_pipeline_v2.py` - Main pipeline script
- `usa_covid_clean.csv` - Cleaned daily data for all states
- `usa_covid_summary.csv` - Summary statistics by state