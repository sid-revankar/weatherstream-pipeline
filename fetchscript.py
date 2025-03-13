import json
import os
from dotenv import load_dotenv
import requests
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
    API_KEY = os.getenv("WEATHERSTACK_API_city_data")
    BASE_URL = "http://api.weatherstack.com/current"
    params = {'access_key':API_KEY, 'query':'Mumbai'}
    current_response = requests.get(BASE_URL, params=params)
    with open("weather_response", "a") as file:
        json.dump(current_response.json(), file, indent=4)
    return current_response.json()

def multi_weather():
    API_KEY = os.getenv("API_KEY")
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    weather = []
    for cities in indian_cities:
        params = {'q':cities,'appid':API_KEY,'units':'metric'}
        multi_weather_response = requests.get(BASE_URL,params)
        weather.append(multi_weather_response.json())
    with open("weatherList",'w') as list_file:
        json.dump(weather, list_file, indent=4)
    return weather

# def extract():
#     weather_list = []
#     with open('weatherList','r') as file:
#         data = json.loads(file.read())
#     for city_data in data:
#         city_weather = {
#             'city':city_data['name'],
#             'temperature':city_data['main']['temp'],
#             'humidity':city_data['main']['humidity'],
#             'wind speed':city_data['wind']['speed'],
#             'wind direction':city_data['wind']['deg']
#         }
#         weather_list.append(city_weather)
#     return weather_list

def exit_program():
    print("Exiting program.")
    exit()

while True:
    print("\nChoose an option:")
    print("1. Fetch Weather Data For Single City Using: 'weatherstack.com' ")
    print("2. Fetch Weather Data For Multiple Cities Using: 'openweathermap.org'")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    match choice:
        case "1":
            weather()
            print(f"Weather data fetched!")
        case "2":
            multi_weather()
            print(f"Weather data fetched!")
        case "3":
            exit_program()
        case _:
            print("Invalid choice! Please enter a valid option.")