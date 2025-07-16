# kafka_producer.py
import pandas as pd
import json
from kafka import KafkaProducer
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

df = pd.read_csv('data/tweet_dataset.csv', encoding='ISO-8859-1')  # UTF-8 fails sometimes

# Use only relevant columns
for index, row in df.iterrows():
    message = {
        "tweet_id": row[0],
        "datetime": row[2],
        "username": row[4],
        "text": row[5]
    }
    producer.send('test-topic', value=message)
    print("✅ Sent:", message)
    time.sleep(1)
