from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}"