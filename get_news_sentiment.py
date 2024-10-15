import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_news_sentiment(query):
    api_key = "YOUR_NEWSAPI_KEY"  # Replace with your actual NewsAPI key
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    
    try:
        # Make the API request to NewsAPI
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        
        # Parse the response to extract articles
        articles = response.json().get('articles', [])
        
        # Initialize VADER sentiment analyzer
        analyzer = SentimentIntensityAnalyzer()
        
        # Calculate sentiment for each article title
        sentiment_scores = []
        for article in articles:
            title = article.get('title', '')
            if title:  # Ensure title exists
                sentiment = analyzer.polarity_scores(title)['compound']
                sentiment_scores.append(sentiment)
        
        # Calculate average sentiment
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
        return avg_sentiment
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None

# Example usage:
query = "climate change"
avg_sentiment = get_news_sentiment(query)
print(f"Average sentiment for '{query}': {avg_sentiment}")
