from kafka import KafkaConsumer
import json
from config import KAFKA_BROKER

consumer = KafkaConsumer(
    'weather-data',
    bootstrap_servers=KAFKA_BROKER,
    group_id='alert_group',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🚨 Weather Alert Consumer Started...")

for message in consumer:
    data = message.value
    city = data['city']
    temperature = data['temperature']
    wind_speed = data['wind_speed']

    if temperature > 35:
        print(f"🔥 Heatwave Alert in {city}! Temp: {temperature}°C")
    elif wind_speed > 10:
        print(f"🌪️ High Wind Alert in {city}! Wind Speed: {wind_speed} km/h")
    else:
        continue