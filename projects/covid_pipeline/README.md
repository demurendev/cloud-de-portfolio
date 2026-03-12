# COVID-19 Data Pipeline

## Overview
An end-to-end data pipeline that ingests, transforms, and analyzes US COVID-19 data across all 50 states.

## Tech Stack
- Python 3
- Pandas
- NY Times COVID-19 Dataset

## What It Does
- Ingests real COVID data directly from source URL
- Calculates daily new cases and deaths per state
- Computes 7-day rolling average to smooth trends
- Generates state-level summary with total cases, deaths, and peak daily cases
- Exports cleaned data to CSV

## Key Findings
- California had the most total cases: 12.1 million
- Texas and Florida followed with 8.4M and 7.5M respectively
- California's peak single-day cases reached 227,972

## Files
- `covid_pipeline_v2.py` - Main pipeline script
- `usa_covid_clean.csv` - Cleaned daily data for all states
- `usa_covid_summary.csv` - Summary statistics by state