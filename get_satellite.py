import requests

def get_satellite_activity(location, api_key):
    # Example URL (replace with actual satellite data provider's API endpoint)
    satellite_url = f"https://api.earthdata.nasa.gov/activity?location={location}&api_key={api_key}"
    
    try:
        # Make API request to fetch satellite data
        response = requests.get(satellite_url)
        response.raise_for_status()  # Raise error for bad HTTP responses
        
        # Parse the response to extract activity level
        data = response.json()
        if 'activity_level' in data:
            return data['activity_level']
        else:
            print("Activity level data not found.")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching satellite data: {e}")
        return None

# Example usage (replace 'your_api_key' with the actual API key)
location = "New York"
api_key = "your_api_key"
activity_level = get_satellite_activity(location, api_key)

if activity_level is not None:
    print(f"Satellite activity level for {location}: {activity_level}")
else:
    print(f"Could not retrieve satellite data for {location}.")

