###############################################################
# Written by Dan Haub in November 2019                        #
#                                                             #
# The purpose of TweetParser.py is to allow easy traversal    #
# of tweet objects obtained from queries                      #
###############################################################

import twitter
import sys
import codecs
import json
from googletrans import Translator

# Returns a single tweet's text or a list of tweet's texts
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

# Returns a single tweet's language code or a list of tweet's language codes
def GetTweetLanguage(tweet):
    if(type(tweet) is list):
        languages = []
        for singleTweet in tweet:
            languages.append(GetTweetLanguage(singleTweet))
        return languages
    else:
        return tweet['metadata']['iso_language_code']

# Returns a single tweet's time stamp or a list of tweet's time stamps
def GetTweetTimeStamp(tweet):
    if(type(tweet) is list):
        timeStamps = []
        for singleTweet in tweet:
            timeStamps.append(GetTweetTimeStamp(singleTweet))
        return timeStamps
    else:
        return tweet['statuses'][0]['created_at']
