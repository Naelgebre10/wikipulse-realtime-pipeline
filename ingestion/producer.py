import json
import requests

STREAM_URL = "https://stream.wikimedia.org/v2/stream/recentchange"

print("Connecting to Wikimedia stream...")

response = requests.get(STREAM_URL, stream=True)

for line in response.iter_lines():

    if line:

        decoded_line = line.decode("utf-8")

        if decoded_line.startswith("data:"):

            try:
                json_data = decoded_line.replace("data: ", "")

                event = json.loads(json_data)

                # Basic validation
                if "id" in event and "title" in event:

                    print("\nNew Event Received")
                    print("-------------------")
                    print(f"Event ID: {event.get('id')}")
                    print(f"Title: {event.get('title')}")
                    print(f"User: {event.get('user')}")
                    print(f"Bot: {event.get('bot')}")
                    print(f"Type: {event.get('type')}")

            except Exception as e:
                print("Error:", e)