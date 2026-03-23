import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

TICKERS = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
BASE_PRICES = {
    'AAPL': 275.0,
    'GOOGL': 310.0,
    'MSFT': 460.0,
    'AMZN': 225.0,
    'TSLA': 435.0
}

print("Starting stock price producer...")

while True:
    for ticker in TICKERS:
        # Simulate price change
        price_change = random.uniform(-2.0, 2.0)
        BASE_PRICES[ticker] += price_change
        
        message = {
            'ticker': ticker,
            'price': round(BASE_PRICES[ticker], 2),
            'timestamp': datetime.now().isoformat(),
            'volume': random.randint(1000, 50000)
        }
        
        producer.send('stock-prices', value=message)
        print(f"Sent: {message}")
    
    time.sleep(2)  # Send every 2 seconds