# Imports
import pandas as pd
import spacy
from textblob import TextBlob
nlp = spacy.load("en_core_web_sm")

"""
Functions
"""
# For removing stopwords in reviews
def remove_stopwords(review):
    # Splitting each review into individual words
    review_words = review.split()
    # Creating a list for cleaned words to append to
    cleaned_words = []
    # Loop through splitted words and filter out the stopwords
    for word in review_words:
        if word.lower() not in stopwords:
            cleaned_words.append(word)
    # Combining the cleaned words into a sentence and return the sentence
    return " ".join(cleaned_words)


# For getting sentiment of a review
def get_sentiment(review):
    return TextBlob(review).polarity


# For categorising the sentiment into positive, negative or neutral
def sentiment_category(score):
    if score <= -0.01:
        return "Negative"
    elif score >= 0.01:
        return "Positive"
    else:
        return "Neutral"


"""
Sentiment Analysis using amazon product review dataset from
https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products
"""
# Reading in csv file
df = pd.read_csv("amazon_product_reviews.csv")

# Selecting the review column and make into a dataframe
data = df["reviews.text"]
data = data.to_frame(name="Review")

# Initialising the stopwords variable
stopwords = nlp.Defaults.stop_words

# Removing the stopwords from the dataframe
cleaned_reviews = data["Review"].apply(lambda x: remove_stopwords(x))

# Generate sentiment polarity scores for each review and create a new column to dataframe
data["Polarity Score"] = cleaned_reviews.apply(get_sentiment)
# Sorting the polarity scores into negative, neutral and positive sentiments and create a new column to dataframe
data["Sentiment Prediction"] = data["Polarity Score"].apply(sentiment_category)


# Getting user to test model on sample product reviews
while True:
    try:
        index = int(input("Please select a review using an index number: \n"))
        if index not in range(28332):
            raise ValueError("Index out of range. Please enter a number between 0 and 28331.")
    except ValueError:
        print("Invalid input.")
    else:
        break
# Printing the review and its predicted sentiment
print(f"Review: {data["Review"][index]}")
print(f"Predicted Sentiment: {data["Sentiment Prediction"][index]}")