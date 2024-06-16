# Sentiment Analysis of Amazon Reviews
Sentiment analysis of reviews of Amazon products to determine whether the emotional tone of the reviews is positive, negative, or neutral.

## Description of Dataset
The dataset used in this task is the "Amazon Product Reviews" dataset from Kaggle, which contains customer reviews of various Amazon products. The column "reviews.text" is used specifically for this task, where sentiment analysis of the reviews has been carried out on 28332 observations.

## Instructions to Run

**Required packages**

pandas==2.2.2

spacy==3.7.5

textblob==0.15.3

**To check if the program works, just run:**
```
python sentiment_analysis.py
```
It will then ask you to input a number. Ensure the number you enter is between 0 and 28331 (inclusive).

**Sample output:**
```
Please select a review using an index number:
420
Review: Love these batt's! Long life! works great in toys all other items!
Predicted Sentiment: Positive
```
The program will prompt you to enter a number again if the input doesn't fulfill the requirements. Example output when the input is invalid:
```
Please select a review using an index number: 
text
Invalid input: invalid literal for int() with base 10: 'text'. Please enter a number between 0 and 28331.
Please select a review using an index number: 
-1
Invalid input: Index out of range. Please enter a number between 0 and 28331.
Please select a review using an index number: 
```

## Evaluation of Results
The sentiment analysis results are evaluated and presented via the following metrics:
1. Polarity Score: The polarity score of the reviews are calculated using the TextBlob library. The polarity score ranges from -1 to 1, indicating from negative to positive(which was checked and established in the notebook.)
2. Categorised Sentiment Prediction: Based on the polarity score, each review is categorised into one of three sentiment classes: Negative (score ≤ -0.01), Neutral (-0.01 < score < 0.01), and Positive (score ≥ 0.01). I chose the boundaries so that there is a little bit of a buffer for the neutral category.
3. Sampling Inspection: In the notebook, random samples of observations were displayed showing the review, polarity score and the prediction.
4. User Testing: In the Python script, users are prompted to input an index number to retrieve the review and its sentiment analysis result, allowing for manual inspection of the predictions.

## Insights into the Model's Strengths and Limitations
Strengths:
- The use of the TextBlob library for sentiment analysis is straightforward and provides easily interpretable polarity scores that range from -1 to 1.
- The removal of the stopwords are efficient and helps the model to focus on more meaningful words in the reviews.
- The “positive”, “negative”, and “neutral” categories provide a straightforward summary.

Limitations:
- The removal of the stopwords could include useful information that reverts the meaning of the review, such as when ‘not’ has been removed.
- When categorised, the model uses a narrow range for classifying neutral sentiments, with the boundaries being manually specified.
- For very large datasets, the current preprocessing steps and sentiment analysis method might be slow and less efficient.
