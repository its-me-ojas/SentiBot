from textblob import TextBlob

user_input = input("Enter a sentence: ")

blob = TextBlob(user_input)
sentiment_score = blob.sentiment.polarity

if sentiment_score > 0:
    print("Positive sentiment!")
elif sentiment_score < 0:
    print("Negative sentiment!")
else:
    print("Neutral sentiment!")
