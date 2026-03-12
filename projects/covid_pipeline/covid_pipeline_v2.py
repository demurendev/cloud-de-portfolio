# Project 1: COVID-19 Data Pipeline
# Ingests, cleans, and analyzes US COVID data by state
# Data source: NY Times COVID-19 Dataset

import pandas as pd

# ---- STEP 1: INGEST ----
print("Downloading COVID data...")
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
df = pd.read_csv(url)
print(f"Loaded {len(df)} rows, {df['state'].nunique()} states")

# ---- STEP 2: TRANSFORM ----
print("Transforming data...")
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(['state', 'date'])
df['new_cases'] = df.groupby('state')['cases'].diff()
df['new_deaths'] = df.groupby('state')['deaths'].diff()
df['7day_avg_cases'] = df.groupby('state')['new_cases'].transform(
    lambda x: x.rolling(7).mean()
)

# ---- STEP 3: ANALYZE ----
print("Analyzing data...")
summary = df.groupby('state').agg(
    total_cases=('cases', 'max'),
    total_deaths=('deaths', 'max'),
    peak_daily_cases=('new_cases', 'max')
).reset_index()

summary = summary.sort_values('total_cases', ascending=False)

print("\nTop 5 states by total cases:")
print(summary.head())

# ---- STEP 4: SAVE ----
print("\nSaving results...")
df.to_csv("usa_covid_clean.csv", index=False)
summary.to_csv("usa_covid_summary.csv", index=False)
print("Done! Files saved.")