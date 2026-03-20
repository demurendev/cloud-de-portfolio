import requests
import boto3
import pandas as pd
from io import StringIO
from datetime import datetime
import time

# Config
API_KEY = '76UJGGQJ0TLJQ369'
BUCKET = 'deborah-de-projects-2026'
TICKERS = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

def get_stock_data(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={API_KEY}&outputsize=compact&datatype=csv'
    response = requests.get(url)
    df = pd.read_csv(StringIO(response.text))
    df['ticker'] = ticker
    return df

def upload_to_s3(df, ticker):
    s3 = boto3.client('s3')
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    key = f'stock-market/raw/{ticker}_{datetime.now().strftime("%Y%m%d")}.csv'
    s3.put_object(Bucket=BUCKET, Key=key, Body=csv_buffer.getvalue())
    print(f'Uploaded {ticker} to s3://{BUCKET}/{key}')

def main():
    for ticker in TICKERS:
        print(f'Fetching {ticker}...')
        df = get_stock_data(ticker)
        upload_to_s3(df, ticker)
        print(f'{ticker} done!')
        time.sleep(15)  # wait 15 seconds between API calls

if __name__ == '__main__':
    main()
