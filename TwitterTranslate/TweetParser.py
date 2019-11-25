###############################################################
# Written by Dan Haub in November 2019                        #
#                                                             #
# The purpose of TweetParser.py is to allow easy traversal    #
# of tweet objects obtained from queries                      #  
#                                                             #
# Updated by Peter Chen in November 2019                      #
###############################################################

import twitter
import sys
import codecs
import json
from googletrans import Translator
import tweepy

authenticated = False

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
tweepyApi = tweepy.API(auth2)

def Authenticate(CONSUMER_KEY_, CONSUMER_SECRET_):
    global CONSUMER_KEY
    global CONSUMER_SECRET

    CONSUMER_KEY = CONSUMER_KEY_
    CONSUMER_SECRET = CONSUMER_SECRET_

    global auth2
    global tweepyApi

    auth2 = tweepy.OAuthHandler(CONSUMER_KEY_, CONSUMER_SECRET_)
    tweepyApi = tweepy.API(auth2)

    print("HERE IN TWEET_PARSER")
    global authenticated
    authenticated = True

# Returns a single tweet's text or a list of tweet's texts
def GetTweetText(tweet):
    if not authenticated: 
        raise Exception('Twitter Api not authenticated')

    if(type(tweet) is list):
        texts = []
        for singleTweet in tweet:
            texts.append(GetTweetText(singleTweet))
        return texts
    else:
        status = tweepyApi.get_status(str(tweet['id']), tweet_mode="extended")
        try:
            return str(status.retweeted_status.full_text)
        except AttributeError:  # Not a Retweet
            return str(status.full_text)
  

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
