# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
<<<<<<< HEAD
#import os
import json

#from TwitterTranslate import TranslationHandler

#dir = os.path.dirname(__file__)
#filename = os.path.join(dir, '..\')
=======
import os
import json
#from TwitterTranslate import TranslationHandler

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '..\SentimentScoreLibraries\SentimentAnalysis.json')
>>>>>>> 89f3eed696d1891f9e068bb17073a5087fbbdeef


with open(filename) as myFile:
    googleAuth = myFile.read()

print(googleAuth)
googleAuth = json.dumps(googleAuth)

print(googleAuth)

exit()
#Instantiates a client
client = language.LanguageServiceClient()

<<<<<<< HEAD
#The text to analyze
tweet = {'text':"Today has been a very bad day today.", 'lang': "en"}
t = json.dumps(tweet)

document = types.Document(
    content=t,
    type=enums.Document.Type.PLAIN_TEXT)

=======
>>>>>>> 89f3eed696d1891f9e068bb17073a5087fbbdeef
#Sentiment Score Function
def SentimentScore(tweet):
    #checks if tweet is a list
    if(type(tweet) is list):
        scores = []
        for singleTweet in tweet:
            scores.append(SentimentScore(singleTweet))
        return scores
    else:
<<<<<<< HEAD
        scores = 0
=======
        score = 0
        document = types.Document(
            content=tweet,
            type=enums.Document.Type.PLAIN_TEXT)
>>>>>>> 89f3eed696d1891f9e068bb17073a5087fbbdeef

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment

        #displays text and language
        #for i in tweet :
        #    print('{}:'.format(i))
        #    print('{}'.format(tweet[i]))
        #    print()

        #displays sentiment score
        #print("Sentiment Score: ")
        score = sentiment.score
        return score

#The text to analyze
tweet = {'text':"Today has been a very bad day today.", 'lang': "en"}

#checks to see if output is correct.
#uncomment to see if it works
print(SentimentScore(tweet))
