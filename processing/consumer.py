import json
import requests
from pymongo import MongoClient

STREAM_URL = "https://stream.wikimedia.org/v2/stream/recentchange"

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")

db = client["wikipulse"]

collection = db["wiki_events"]

print("Connected to MongoDB...")
print("Listening to Wikipedia stream...")

processed_ids = set()

response = requests.get(STREAM_URL, stream=True)

for line in response.iter_lines():

    if line:

        decoded_line = line.decode("utf-8")

        if decoded_line.startswith("data:"):

            try:
                json_data = decoded_line.replace("data: ", "")

                event = json.loads(json_data)

                event_id = event.get("id")

                # Skip duplicates
                if event_id in processed_ids:
                    continue

                processed_ids.add(event_id)

                cleaned_event = {
                    "event_id": event.get("id"),
                    "title": event.get("title"),
                    "user": event.get("user"),
                    "bot": event.get("bot", False),
                    "timestamp": event.get("timestamp"),
                    "type": event.get("type"),
                    "server_name": event.get("server_name"),
                    "comment": event.get("comment")
                }

                # Insert into MongoDB
                collection.insert_one(cleaned_event)

                print(f"Inserted: {cleaned_event['title']}")

            except Exception as e:
                print("Processing Error:", e)