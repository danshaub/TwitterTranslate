# Author:  Dan Haub
# Chapman Email:  haub@chapman.edu
# Author:  Peter Chen
# Chapman Email:  haichen@chapman.edu
# Author:  Vincent Jodjana
# Chapman Email:  jodjana@chapman.edu
# Course Number and Section:  CPSC 353-02

# Twitter Translate [SentimentAnalysis.py]

# The purpose of SentimentAnalysis.py is to serve
# as a simplified wrapper module for Google's
# natural language processing API

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
import json

# Collects Google API authentication
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'Files/GoogleAuth.json')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = filename

#Instantiates a google api client
client = language.LanguageServiceClient()

#The text to analyze
tweet = {'text':"Today has been a very bad day today.", 'lang': "en"}
t = json.dumps(tweet)

#Sentiment Score Function
def SentimentScore(tweet):
    #checks if tweet is a list and if so, calculates average sentiment score
    if(type(tweet) is list):
        scores = []
        for singleTweet in tweet:
            scores.append(SentimentScore(singleTweet))

        total = 0
        for score in scores:
            total = total + score
        
        avg = ''
        if(total == 0):
            avg = 0
        else:
            avg = total/len(scores)
        return avg
    # Otherwise calculates the sentiment on a single tweet
    else:
        score = 0
        document = types.Document(content=tweet, type=enums.Document.Type.PLAIN_TEXT)

        # Calculates the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        
        score = sentiment.score
        return score
