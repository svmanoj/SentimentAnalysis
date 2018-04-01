import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
#nltk.download('punkt')
#nltk.download('vader_lexicon')
def getSen(a):
    sentence = a
    print(sentence)
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    """for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), '')"""
    return ss['compound']