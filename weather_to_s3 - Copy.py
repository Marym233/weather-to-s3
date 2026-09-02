"""
Simple Python + AWS project: fetch weather data and save it to S3.

What this does:
1. Calls a free weather API to get current weather for a city
2. Saves that data as a JSON file
3. Uploads the JSON file to an AWS S3 bucket

Before running, you need:
- A free API key from https://openweathermap.org/api (sign up, takes 2 min)
- An AWS account with an S3 bucket already created
- AWS credentials configured on your machine (see step-by-step guide)
"""

import json
import requests
import boto3
from datetime import datetime

# ---- CONFIG: fill these in ----
API_KEY = "Your_API_Key"
CITY = "Portlaoise"
BUCKET_NAME = "Your_Bucket_Name"
# --------------------------------

def get_weather(city, api_key):
    """Fetch current weather data for a city."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    response.raise_for_status()  # raises an error if the request failed
    return response.json()

def save_to_s3(data, bucket_name):
    """Save weather data as a JSON file in an S3 bucket."""
    s3 = boto3.client("s3")

    # create a filename with today's date, e.g. weather_2026-09-02.json
    filename = f"weather_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.json"

    # convert the data to a JSON string
    json_data = json.dumps(data, indent=2)

    # upload it to S3
    s3.put_object(Bucket=bucket_name, Key=filename, Body=json_data)

    print(f"Uploaded {filename} to bucket '{bucket_name}'")

def main():
    print(f"Fetching weather for {CITY}...")
    weather_data = get_weather(CITY, API_KEY)

    print("Saving to S3...")
    save_to_s3(weather_data, BUCKET_NAME)

    print("Done!")

if __name__ == "__main__":
    main()
