import twitter
import sys
import codecs
import json
from googletrans import Translator

def GetTweetText(tweet):
    if(type(tweet) is list):
        texts = []
        for singleTweet in tweet:
            texts.append(GetTweetText(singleTweet))
        return texts
    else:
        if(tweet['truncated']):
            return "[TRUNCATED]:  " + tweet['text']
        else:
            return tweet['text']

def GetTweetLanguage(tweet):
    if(type(tweet) is list):
        languages = []
        for singleTweet in tweet:
            languages.append(GetTweetLanguage(singleTweet))
        return languages
    else:
        return tweet['metadata']['iso_language_code']

def GetTweetTimeStamp(tweet):
    if(type(tweet) is list):
        timeStamps = []
        for singleTweet in tweet:
            timeStamps.append(GetTweetTimeStamp(singleTweet))
        return timeStamps
    else:
        return tweet['statuses'][0]['created_at']
