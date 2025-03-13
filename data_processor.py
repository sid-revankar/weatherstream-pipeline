import json
import pandas as pd
from datetime import datetime, timezone

def extract_relevant_data(json_data):
    extracted_data = {
        "timestamp": datetime.fromtimestamp(json_data["dt"], timezone.utc).date(),
        "temperature": json_data["main"]["temp"],
        "humidity": json_data["main"]["humidity"],
        "wind_speed": json_data["wind"]["speed"],
        "city": json_data["name"]
    }
    return extracted_data

def transform_weather_data(raw_data):
    df = pd.DataFrame(raw_data)
    
    daily_avg = df.groupby(['timestamp', 'city']).agg({
        'temperature': 'mean',
        'humidity': 'mean',
        'wind_speed': 'mean'
    }).reset_index()

    return daily_avg

# Load JSON file
with open("weatherList", "r") as file:
    data_list = json.load(file)

# If data_list is a single JSON object, wrap it in a list
if isinstance(data_list, dict):  
    data_list = [data_list]

# Extract and transform data
extracted_data = [extract_relevant_data(entry) for entry in data_list]
processed_data = transform_weather_data(extracted_data)

# Display output
print(processed_data)