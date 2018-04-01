import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
#nltk.download('punkt')
#nltk.download('vader_lexicon')
sentence = input()
sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sentence)
print(ss['compound']) 

