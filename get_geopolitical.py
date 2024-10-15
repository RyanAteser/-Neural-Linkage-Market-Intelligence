def get_geopolitical_risk(query):
    gdelt_url = f'https://api.gdeltproject.org/api/v2/doc/doc?query={query}&mode=artlist&format=json'
    response = requests.get(gdelt_url)
    events = response.json()['articles']
    
    # Process the events to get risk ratings (custom)
    risk_score = sum(event.get('tone', {}).get('polarity', 0) for event in events) / len(events)
    
    return risk_score
