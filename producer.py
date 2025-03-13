from kafka import KafkaProducer
import json
import requests
from config import KAFKA_BROKER, TOPIC_NAME, WEATHER_API_URL, WEATHER_API_KEY, CITIES

# main function to fetch weather data.
def fetch_weather_data(city):
    params = {'q':city,'appid':WEATHER_API_KEY,'units':'metric'}
    response = requests.get(WEATHER_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": round(data["wind"]["speed"] * 3.6, 2)
        }
    else:
        print(f"⚠️ Failed to fetch weather data for {city}")
        return None

# Kafka Producer.
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# loop for each city weather data.
for city in CITIES:
    weather_data = fetch_weather_data(city)
    if weather_data:
        producer.send(TOPIC_NAME["weather-data"]["topic"], value=weather_data)
        print(f"✅ Sent weather data: {weather_data}")

# Close producer after sending all data.
producer.flush()
producer.close()

print("🚀 Producer finished. Data sent for all cities.")