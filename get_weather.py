import requests

def get_weather_data(location):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"

    try:
        # Make the API request to OpenWeatherMap
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        
        # Parse the response JSON
        weather_data = response.json()
        
        # Extract relevant weather features
        temperature = weather_data['main']['temp']  # Temperature is now in Celsius
        wind_speed = weather_data['wind']['speed']  # Wind speed in m/s
        precipitation = weather_data.get('rain', {}).get('1h', 0)  # mm of rain in the last hour
        humidity = weather_data['main']['humidity']  # Percentage of humidity
        weather_description = weather_data['weather'][0]['description']  # Weather condition description

        return {
            'temperature': temperature,
            'wind_speed': wind_speed,
            'precipitation': precipitation,
            'humidity': humidity,
            'weather_description': weather_description
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Example usage (replace with a real location)
location = "New York"
weather_info = get_weather_data(location)

if weather_info:
    print(f"Weather in {location}:")
    print(weather_info)
else:
    print(f"Could not retrieve weather data for {location}.")
