import requests
import pandas as pd
import time
from config import OPENWEATHER_API_KEY, LAT, LON

def fetch_weather_data():
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    data = response.json()

    weather_list = []
    for item in data["list"]:
        weather_list.append({
            "timestamp": item["dt"],
            "temperature": item["main"]["temp"] - 273.15,  # Kelvin to Celsius
            "humidity": item["main"]["humidity"],
            "pressure": item["main"]["pressure"]
        })

    df = pd.DataFrame(weather_list)
    df.to_csv("weather_data.csv", index=False)
    print("Weather data saved.")
    return df
