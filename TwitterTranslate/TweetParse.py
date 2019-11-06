import twitter
import sys
import codecs
import json
from googletrans import Translator

def GetTweetText(tweet):
    if(tweet['truncated']):
        return "[TRUNCATED]:  " + tweet['text']
    else:
        return tweet['text']

def GetTweetLanguage(tweet):
    return tweet['metadata']['iso_language_code']

def GetTweetTimeStamp(tweet):
    return tweet['statuses'][0]['created_at']
