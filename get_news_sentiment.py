import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_news_sentiment(query):
    api_key = "YOUR_NEWSAPI_KEY"
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'

    response = requests.get(url)
    articles = response.json()['articles']

    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = [analyzer.polarity_scores(article['title'])['compound'] for article in articles]
    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

    return avg_sentiment
