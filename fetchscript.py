import json
import os
import random
import time
import pandas as pd
from dotenv import load_dotenv
import matplotlib
matplotlib.use("TkAgg")  # Or try "Qt5Agg"
import matplotlib.pyplot as plt
import requests
from itertools import count
load_dotenv()


indian_cities = [
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
def weather():
    API_city_data = os.getenv("WEATHERSTACK_API_city_data")
    BASE_URL = "https://api.weatherstack.com/current"
    params = {'access_city_data':API_city_data, 'query':'New York'}
    historical_response = requests.get(BASE_URL, params=params)
    with open("weather_response", "a") as file:
        json.dump(historical_response.json(), file, indent=4)
    return historical_response.json()

def multi_weather():
    API_city_data = os.getenv("API_city_data")
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    weather = []
    for cities in indian_cities:
        params = {'q':cities,'appid':API_city_data}
        multi_weather_response = requests.get(BASE_URL,params)
        weather.append(multi_weather_response.json())
    with open("weatherList",'w') as list_file:
        json.dump(weather, list_file, indent=4)
    return weather

# print(multi_weather())
# print(weather())
# print(os.getenv('WEATHERSTACK_API_city_data'))
def extract():
    weather_list = []
    with open('weatherList','r') as file:
        data = json.loads(file.read())
    for city_data in data:
        city_weather = {
            'city':city_data['name'],
            'temperature':city_data['main']['temp'],
            'humidity':city_data['main']['humidity'],
            'wind speed':city_data['wind']['speed'],
            'wind direction':city_data['wind']['deg']
        }
        weather_list.append(city_weather)
    return weather_list

df = pd.DataFrame(extract())
df.index = range(1, len(df) + 1)
print(help(df))



