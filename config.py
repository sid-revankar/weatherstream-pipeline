import os
from dotenv import load_dotenv
load_dotenv()

KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = {
    "weather-data": {
        "topic": "weather-data", 
        "num_partitions": 3,
        "replication_factor": 1
    },
    "weather-alert": {
        "topic": "weather-alert", 
        "num_partitions": 1,
        "replication_factor": 1
    }
}

# API URL
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

# API KEY
WEATHER_API_KEY = os.getenv("API_KEY")

# City List
"""
You can add cities or change the entire city list. 
- Note: This list is missing some cities from India.
"""
CITIES = [
    "Mumbai",        # Maharashtra
    "Delhi",         # Delhi
    "Bengaluru",     # Karnataka
    "Chennai",       # Tamil Nadu
    "Kolkata",       # West Bengal
    "Hyderabad",     # Telangana
    "Ahmedabad",     # Gujarat
    "Pune",          # Maharashtra
    "Jaipur",        # Rajasthan
    "Lucknow",       # Uttar Pradesh
    "Kanpur",        # Uttar Pradesh
    "Visakhapatnam", # Andhra Pradesh
    "Bhopal",        # Madhya Pradesh
    "Indore",        # Madhya Pradesh
    "Coimbatore",    # Tamil Nadu
    "Patna",         # Bihar
    "Agra",          # Uttar Pradesh
    "Madurai",       # Tamil Nadu
    "Vijayawada",    # Andhra Pradesh
    "Mysuru",        # Karnataka
    "Ranchi",        # Jharkhand
    "Dehradun",      # Uttarakhand
    "Guwahati",      # Assam
    "Shillong",      # Meghalaya
    "Kochi",         # Kerala
    "Jodhpur",       # Rajasthan
    "Udaipur",       # Rajasthan
    "Kota",          # Rajasthan
    "Bhubaneswar",   # Odisha
    "Cuttack",       # Odisha
    "Rourkela",      # Odisha
    "Navi Mumbai",   # Maharashtra
    "Faridabad",     # Haryana
    "Gurgaon",       # Haryana
    "Noida",         # Uttar Pradesh
    "Ghaziabad",     # Uttar Pradesh
    "Siliguri",      # West Bengal
    "Bikaner",       # Rajasthan
    "Ajmer",         # Rajasthan
    "Jaisalmer",     # Rajasthan
    "Mangalore",     # Karnataka
    "Belgaum",       # Karnataka
    "Kolhapur"      # Maharashtra
]