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
import tweepy

# Creates twitter api object
CONSUMER_KEY = 'It4voosHW6TyL6iVjvzPiirqk'
CONSUMER_SECRET = 'f1fCFFwbz80qUxLpO155Btzn1HPV0N2fXgatZVLCPVAj7xoVE7'
OAUTH_TOKEN = '979943818991616000-i2OzeJ71Y288wBWrMlw6zJcRIlwD676'
OAUTH_TOKEN_SECRET = '4SADdllXvyPFyKur7eFrV3AfqaxffezU1F5tgKx2ikdzJ'

# auth for tweppy library
auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth2)

# Returns a single tweet's text or a list of tweet's texts
def GetTweetText(tweet):
    if(type(tweet) is list):
        texts = []
        for singleTweet in tweet:
            texts.append(GetTweetText(singleTweet))
        textsEnglish = texts
    else:
        if(tweet['truncated']):
            return tweet['id']
        else:
            return tweet['id']

    count = 1

    for text in textsEnglish:
        status = api.get_status(str(text), tweet_mode="extended")
        try:
            print(str(count), ", ", status.retweeted_status.full_text)
        except AttributeError:  # Not a Retweet
            print(str(count), ", ", status.full_text)
        count = count + 1

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


def Get_Consumer_Key():
    return CONSUMER_KEY

def Get_Consumer_Secret():
    return CONSUMER_SECRET

def Get_Oauth_Token():
    return OAUTH_TOKEN

def Get_Token_Secret():
    return OAUTH_TOKEN_SECRET
