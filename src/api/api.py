# src/api.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory list to store tweets (temporarily)
tweets = []

class Tweet(BaseModel):
    id: int
    text: str
    username: str

@app.get("/")
def home():
    return {"message": "Twitter Kafka API is live ✅"}

@app.get("/tweets", response_model=List[Tweet])
def get_all_tweets():
    return tweets

@app.post("/tweets")
def add_tweet(tweet: Tweet):
    tweets.append(tweet)
    return {"message": "Tweet added"}
