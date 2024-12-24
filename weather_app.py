import requests
import sys

API_KEY = 'your_openweathermap_api_key_here'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] != 200:
        print(f"Error: {data['message']}")
        return

    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"Weather in {city}:")
    print(f"Description: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python weather_app.py <city>")
        sys.exit(1)

    city = sys.argv[1]
    get_weather(city)
