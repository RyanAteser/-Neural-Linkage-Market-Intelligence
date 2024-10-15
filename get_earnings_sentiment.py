import yfinance as yf
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def get_earnings_sentiment(symbol):
    # Fetch company data from Yahoo Finance
    stock = yf.Ticker(symbol)
    
    # Fetch earnings data
    earnings = stock.earnings
    if earnings.empty:
        print(f"No earnings data available for {symbol}.")
        return None

    # Convert earnings DataFrame to string for sentiment analysis
    earnings_text = earnings.to_string()
    
    # Perform sentiment analysis on earnings data
    sentiment = analyzer.polarity_scores(earnings_text)['compound']
    
    print(f"Earnings sentiment for {symbol}: {sentiment}")
    return sentiment

# Example usage
symbol = "AAPL"  # Apple
get_earnings_sentiment(symbol)
