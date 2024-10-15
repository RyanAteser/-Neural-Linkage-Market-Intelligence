def get_commodity_prices(commodity):
    # Fetch real-time commodity prices (oil, gold, etc.)
    commodity_url = f"https://api.commodities.com/prices/{commodity}"
    response = requests.get(commodity_url)
    return response.json()['price']
