# 🐦 Twitter Stream Kafka Project

This project simulates real-time tweet streaming using **Apache Kafka** and **FastAPI**, reading tweets from a CSV file and exposing APIs for interaction.

---

## 📁 Project Structure
twitter-stream-project/
├── data/
│ └── tweet_dataset.csv # Source dataset
├── src/
│ ├── kafka_producer.py # Sends tweets to Kafka
│ ├── kafka_consumer.py # Consumes tweets from Kafka
│ └── api/
│ └── api.py # FastAPI server
├── requirements.txt
└── README.md
---

##  Setup & Run

### 1.  Prerequisites
- Python 3.10+ (Python 3.13 supported)
- Kafka running locally (`localhost:9092`)
- Virtualenv recommended

### 2.  Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate

### 3.  Install dependencies
pip install -r requirements.txt

### 4.  Start Zookeeper and Kafka server using:
# In terminal 1
bin/zookeeper-server-start.sh config/zookeeper.properties
# In terminal 2
bin/kafka-server-start.sh config/server.properties

### 5.  Run Kafka Producer
python src/kafka_producer.py

### 6.  Run Kafka Consumer
python src/kafka_consumer.py

### 7.  Start FastAPI Server
uvicorn src.api.api:app --reload