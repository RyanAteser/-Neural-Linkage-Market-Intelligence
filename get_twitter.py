import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_twitter_data(ticker):
    # Twitter API credentials
    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    # Authenticate with Twitter
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get recent tweets about the ticker
    tweets = api.search_tweets(q=ticker, count=100, lang='en', result_type='recent')

    # Analyze sentiment of tweets
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = [analyzer.polarity_scores(tweet.text)['compound'] for tweet in tweets]
    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

    return avg_sentiment
