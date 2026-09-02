# Weather to S3

A simple Python project that fetches live weather data from a public API and stores it in an AWS S3 bucket as JSON.

## What it does
- Calls the OpenWeatherMap API to get current weather for a given city
- Converts the response into a JSON file
- Uploads that file to an AWS S3 bucket using boto3

## Tech used
- Python
- AWS S3 (via boto3)
- OpenWeatherMap API

## Why I built this
I wanted to understand how a simple data pipeline works end-to-end — calling an external API, processing the response, and storing it in the cloud — as part of building my software development skills ahead of internship applications.

## Next steps
- Automate it to run daily using AWS Lambda + EventBridge
- Compare weather trends across multiple cities over time
