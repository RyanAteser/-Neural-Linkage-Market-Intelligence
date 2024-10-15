import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_reddit_data(ticker):
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET', user_agent='YOUR_USER_AGENT')

    # Search Reddit for the ticker
    posts = reddit.subreddit('wallstreetbets').search(ticker, limit=100)

    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = [analyzer.polarity_scores(post.title)['compound'] for post in posts]
    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

    return avg_sentiment
