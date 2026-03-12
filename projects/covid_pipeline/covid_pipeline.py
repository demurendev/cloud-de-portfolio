# COVID-19 Data Pipeline
# Downloads real data, cleans it, analyzes it, saves results

import pandas as pd
import requests

# ---- STEP 1: DOWNLOAD THE DATA ----
print("Downloading COVID data...")
url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
df = pd.read_csv(url)
print(f"Downloaded {len(df)} rows of data")

# ---- STEP 2: FILTER TO USA ONLY ----
print("Filtering to USA...")
usa = df[df["state"] == "New York"]
print(f"USA has {len(usa)} rows")

# ---- STEP 3: KEEP ONLY COLUMNS WE NEED ----
usa = usa[["date", "cases", "deaths"]]

# ---- STEP 4: CALCULATE 7-DAY ROLLING AVERAGE ----
print("Calculating 7-day rolling average...")


# ---- STEP 5: SAVE TO CSV ----
print("Saving results...")
usa.to_csv("usa_covid_clean.csv", index=False)
print("Done! File saved as usa_covid_clean.csv")