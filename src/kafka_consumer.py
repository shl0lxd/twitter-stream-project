# src/kafka_consumer.py

from kafka import KafkaConsumer
import json

def safe_json_deserializer(message):
    try:
        decoded = message.decode('utf-8')
        if not decoded.strip():
            raise ValueError("Empty message")
        return json.loads(decoded)
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as e:
        print(f"❌ Skipped malformed message: {e}")
        return None

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='twitter-group',
    value_deserializer=safe_json_deserializer
)

print("✅ Listening for messages...\n")

for message in consumer:
    if message.value:  # skip if deserialization failed
        print("🔹 Received:", message.value)
