# Music Streaming Batch Pipeline 🎵

## Overview
A batch data processing pipeline that validates, transforms and analyzes music streaming data. Built to demonstrate data quality validation, branching logic and KPI calculations using Apache Airflow orchestration.

## Architecture
S3 (raw CSVs) → Airflow DAG → Data Validation → KPI Calculations → Redshift

## Tech Stack
Python, Pandas, AWS S3, boto3, Amazon Redshift, Apache Airflow

## Dataset
Songs, users and streaming data across 3 stream files containing listening history

## Airflow DAG Tasks
1. validate_datasets checks all CSV files have required columns
2. check_validation uses BranchPythonOperator to route based on validation results
3. calculate_genre_level_kpis computes popularity index and average duration by genre
4. calculate_hourly_kpis computes unique listeners and top artist per hour
5. move_processed_files archives processed stream files

## Key Concepts Demonstrated
Data quality validation before processing
Branching logic with BranchPythonOperator
XCom for passing data between tasks
Batch processing with Pandas
Upsert pattern