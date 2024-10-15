import requests

# Your Alpha Vantage API key
api_key = 'your_alpha_vantage_api_key'

# A dictionary to hold the symbols of common commodities
commodities = {
    'Crude Oil (WTI)': 'CL=F',
    'Brent Oil': 'BZ=F',
    'Gold': 'GC=F',
    'Silver': 'SI=F',
    'Natural Gas': 'NG=F',
    'Copper': 'HG=F',
    'Platinum': 'PL=F',
    'Palladium': 'PA=F'
}

def get_commodity_price(commodity_name, commodity_symbol):
    url = f'https://www.alphavantage.co/query'
    
    # Parameters for the API request
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': commodity_symbol,
        'apikey': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract the time series data
        time_series = data.get("Time Series (Daily)", {})
        
        if not time_series:
            print(f"No data available for {commodity_name} ({commodity_symbol})")
            return None

        latest_date = next(iter(time_series))
        latest_data = time_series[latest_date]
        
        print(f"Latest data for {commodity_name} ({commodity_symbol}) on {latest_date}:")
        print(f"Open: {latest_data['1. open']}, High: {latest_data['2. high']}, Low: {latest_data['3. low']}, Close: {latest_data['4. close']}")
        
        return latest_data['4. close']  # You can return other fields if needed
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred fetching data for {commodity_name}: {e}")
        return None

# Iterate over the commodities and fetch prices for each
for commodity_name, commodity_symbol in commodities.items():
    get_commodity_price(commodity_name, commodity_symbol)
