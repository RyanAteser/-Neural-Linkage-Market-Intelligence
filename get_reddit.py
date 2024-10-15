import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_reddit_data(ticker):
    # Initialize Reddit API client (make sure to replace with your own credentials)
    reddit = praw.Reddit(client_id='YOUR_CLIENT_ID', 
                         client_secret='YOUR_CLIENT_SECRET', 
                         user_agent='YOUR_USER_AGENT')

    try:
        # Search Reddit for posts mentioning the ticker in the WallStreetBets subreddit
        posts = reddit.subreddit('wallstreetbets').search(ticker, limit=100)
        
        analyzer = SentimentIntensityAnalyzer()
        sentiment_scores = []
        
        for post in posts:
            # Analyze both the title and the selftext (if available) for sentiment
            title_sentiment = analyzer.polarity_scores(post.title)['compound']
            body_sentiment = analyzer.polarity_scores(post.selftext)['compound'] if post.selftext else 0
            combined_sentiment = (title_sentiment + body_sentiment) / 2  # Average the title and body sentiment
            
            sentiment_scores.append(combined_sentiment)
        
        # Calculate average sentiment score across all posts
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
        return avg_sentiment
    
    except Exception as e:
        print(f"Error fetching Reddit data: {e}")
        return None

# Example usage:
ticker = "GME"  # Example ticker symbol (GameStop)
avg_sentiment = get_reddit_data(ticker)
print(f"Average sentiment for {ticker} on Reddit: {avg_sentiment}")
