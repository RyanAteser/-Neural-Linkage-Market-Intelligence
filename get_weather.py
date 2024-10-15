import requests

def get_weather_data(location):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

    response = requests.get(url)
    weather_data = response.json()

    # Extract relevant weather features
    temperature = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    wind_speed = weather_data['wind']['speed']
    precipitation = weather_data.get('rain', {}).get('1h', 0)  # mm in the last hour
    return {'temperature': temperature, 'wind_speed': wind_speed, 'precipitation': precipitation}
