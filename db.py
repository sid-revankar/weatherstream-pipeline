import psycopg2
import json
from datetime import datetime, timezone

# DB connection.
conn = psycopg2.connect(
    dbname="current_weather_data",
    user="weatheradmin", 
    password="12345",
    host="localhost",
    port="5432"
)

currsor = conn.cursor()

# Load JSON
with open('weatherList', 'r') as file:
    data = json.loads(file.read())

# Insert Query
query = """
INSERT INTO weather_data (city_name, temperature, humidity, wind_speed, timestamp)
VALUES (%s, %s,%s, %s, %s)
"""
for entry in data:
    date = datetime.fromtimestamp(entry["dt"], timezone.utc).date()

    currsor.execute(query, (
        entry['name'],
        entry['main']['temp'],
        entry['main']['humidity'],
        entry['wind']['speed'],
        date
    ))

# Commit and close the connection.
conn.commit()
print("Insertion Done...")
currsor.close()
print("Connection Closed!")