import requests

def get_patent_activity(company_name, api_key):
    # Correct API endpoint (replace with actual endpoint based on USPTO documentation)
    patent_url = f"https://developer.uspto.gov/ds-api/patent/application/v1/{company_name}?api_key={api_key}"
    
    try:
        # Make the API request to USPTO
        response = requests.get(patent_url)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        
        # Parse the response to extract patent data
        data = response.json()
        if 'patent_count' in data:
            return data['patent_count']
        else:
            print("Patent count data not found.")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching patent data: {e}")
        return None

# Example usage (you need to replace 'your_api_key' with a valid USPTO API key)
company_name = "Apple"
api_key = "your_api_key"
patent_count = get_patent_activity(company_name, api_key)

if patent_count is not None:
    print(f"{company_name} has {patent_count} patents.")
else:
    print(f"Could not retrieve patent data for {company_name}.")
