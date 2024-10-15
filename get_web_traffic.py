from pytrends.request import TrendReq

def get_google_trends_data(ticker):
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # Build payload with the search query
    pytrends.build_payload([ticker], cat=0, timeframe='today 12-m')
    
    # Get interest over time
    trends_data = pytrends.interest_over_time()
    
    return trends_data

# Example usage:
ticker = "AAPL"  # Example ticker (Apple)
trends_data = get_google_trends_data(ticker)
print(trends_data)
