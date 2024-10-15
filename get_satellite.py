def get_satellite_activity(location):
    # Example placeholder for fetching satellite data
    satellite_url = f"https://api.satellite.com/activity?location={location}"
    response = requests.get(satellite_url)
    return response.json()['activity_level']
