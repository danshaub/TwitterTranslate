# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
import json
#from TwitterTranslate import TranslationHandler

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '..\SentimentScoreLibraries\SentimentAnalysis.json')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = filename

#Instantiates a client
client = language.LanguageServiceClient()

#The text to analyze
tweet = {'text':"Today has been a very bad day today.", 'lang': "en"}
t = json.dumps(tweet)

document = types.Document(
    content=t,
    type=enums.Document.Type.PLAIN_TEXT)

#Sentiment Score Function
def SentimentScore(tweet):
    #checks if tweet is a list
    if(type(tweet) is list):
        scores = []
        for singleTweet in tweet:
            scores.append(SentimentScore(singleTweet))
        return scores
    else:
        score = 0
        document = types.Document(content=tweet['text'], type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        
        score = sentiment.score
        return score
