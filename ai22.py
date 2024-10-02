from nltk.sentiment.vader import SentimentIntensityAnalyzer  # Fixed typo
import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()  # Fixed typo

text = input("Enter the text: ")

ss = sia.polarity_scores(text)
print(ss)
