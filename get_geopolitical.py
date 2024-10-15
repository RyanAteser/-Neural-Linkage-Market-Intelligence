import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

def get_country_risk_factor(sourcecountry):
    """
    Assigns a risk factor based on the source country.
    High-risk countries involved in the conflict will have higher risk factors.
    """
    high_risk_countries = {'Russia', 'Ukraine', 'Belarus'}
    medium_risk_countries = {'USA', 'China', 'NATO members'}

    if sourcecountry in high_risk_countries:
        return 1.5  # Increase risk for high-risk countries
    elif sourcecountry in medium_risk_countries:
        return 1.2  # Slightly increase for medium-risk countries
    else:
        return 1  # Default risk for other countries

def get_geopolitical_risk(query):
    gdelt_url = f'https://api.gdeltproject.org/api/v2/doc/doc?query={query}&mode=artlist&format=json'

    try:
        response = requests.get(gdelt_url)
        response.raise_for_status()

        articles = response.json().get('articles', [])

        if not articles:
            print("No articles found for the query.")
            return 0

        total_sentiment = 0
        count = 0

        for article in articles:
            title = article.get('title', '')
            sourcecountry = article.get('sourcecountry', '')

            if title:
                sentiment = analyzer.polarity_scores(title)['compound']

                # Amplify negative sentiment
                if sentiment < 0:
                    sentiment *= 3

                risk_factor = get_country_risk_factor(sourcecountry)
                sentiment *= risk_factor

                total_sentiment += sentiment
                count += 1

        if count == 0:
            print("No valid titles found.")
            return 0

        # Apply scaling factor to the final risk score
        risk_score = -1 * (total_sentiment / count) * 10  # Multiply final score by 10 for larger values
        return risk_score

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example usage:
query = "Russia Ukraine conflict"
risk_score = get_geopolitical_risk(query)
print(f"Geopolitical Risk Score for '{query}': {risk_score}")
