
import requests
import json

# Author: Huzaifa Khan

def fetch_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def main():
    city = "London"
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    weather_data = fetch_weather(city, api_key)
    with open('weather_data.json', 'w') as f:
        json.dump(weather_data, f, indent=4)
    print("Weather data saved to weather_data.json")

if __name__ == "__main__":
    main()
