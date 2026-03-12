# Read COVID data directly from AWS S3
import pandas as pd
import boto3

print("Connecting to S3...")
s3_url = "s3://deborah-covid-pipeline-2026/usa_covid_clean.csv"
df = pd.read_csv(s3_url, storage_options={"anon": False})

print(f"Loaded {len(df)} rows from S3")
print("\nTop 5 states by cases:")
print(df.groupby('state')['cases'].max().sort_values(ascending=False).head())