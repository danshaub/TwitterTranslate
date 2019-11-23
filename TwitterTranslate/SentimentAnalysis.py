# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
#from TwitterTranslate import TranslationHandler

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '..\SentimentScoreLibraries\languageCodes.txt')

#Instantiates a client
client = language.LanguageServiceClient()

#The text to analyze
tweet = {'text':"Today has been a very bad day today.", 'lang': "en"}

#Sentiment Score Function
def SentimentScore(t):
    #checks if tweet is a list
    if(type(t) is list):
        scores = []
        for singleTweet in t:
            scores.append(SetimentScore(singleTweet))
        return scores
    else:
        scores = 0
        document = types.Document(
            content=t,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment

        #displays text and language
        #for i in tweet :
        #    print('{}:'.format(i))
        #    print('{}'.format(tweet[i]))
        #    print()

        #displays sentiment score
        #print("Sentiment Score: ")
        scores = sentiment.score
        return scores

#checks to see if output is correct.
#uncomment to see if it works
print(SentimentScore(t))
