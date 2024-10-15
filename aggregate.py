# data_aggregator.py
import pandas as pd
from data_preprocessing import get_stock_data, get_macro_data, preprocess_data
from social_media_data import get_twitter_data, get_reddit_data
from weather_data import get_weather_data
from news_data import get_news_sentiment
from geopolitical_data import get_geopolitical_risk

def aggregate_data(ticker, location):
    # Get stock and macroeconomic data
    stock_data = get_stock_data(ticker)
    macro_data = get_macro_data()

    # Get additional data sources
    twitter_sentiment = get_twitter_data(ticker)
    reddit_sentiment = get_reddit_data(ticker)
    weather = get_weather_data(location)
    news_sentiment = get_news_sentiment(ticker)
    geopolitical_risk = get_geopolitical_risk(ticker)

    # Add all data to the main dataframe
    stock_data['Twitter_Sentiment'] = twitter_sentiment
    stock_data['Reddit_Sentiment'] = reddit_sentiment
    stock_data['Weather_Temperature'] = weather['temperature']
    stock_data['Weather_Wind_Speed'] = weather['wind_speed']
    stock_data['News_Sentiment'] = news_sentiment
    stock_data['Geopolitical_Risk'] = geopolitical_risk

    # Merge with macroeconomic data
    data = preprocess_data(stock_data, macro_data, twitter_sentiment)

    return data
