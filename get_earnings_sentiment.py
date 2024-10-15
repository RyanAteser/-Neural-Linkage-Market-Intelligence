def get_earnings_call_sentiment(company):
    transcript_url = f"https://api.earningscall.com/transcripts/{company}"
    response = requests.get(transcript_url)
    transcript = response.json()['transcript']
    sentiment = analyzer.polarity_scores(transcript)['compound']
    return sentiment
