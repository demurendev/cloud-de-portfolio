import json
from kafka import KafkaConsumer

# Connect to Kafka and subscribe to stock-prices topic
consumer = KafkaConsumer(
    'stock-prices',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='latest'
)

print("Starting stock price consumer... waiting for messages!")

for message in consumer:
    data = message.value
    print(f"Received: {data['ticker']} | Price: ${data['price']} | Time: {data['timestamp']}")