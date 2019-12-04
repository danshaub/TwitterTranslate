# Author:  Dan Haub
# Chapman Email:  haub@chapman.edu
# Author:  Peter Chen
# Chapman Email:  haichen@chapman.edu
# Author:  Vincent Jodjana
# Chapman Email:  jodjana@chapman.edu
# Course Number and Section:  CPSC 353-02

# Twitter Translate [TweetParser.py]

# The purpose of TweetParser.py is to allow easy traversal
# of tweet dictionaries obtained from queries

import twitter
import sys
import codecs
import json
from googletrans import Translator
import tweepy
import os

authenticated = False

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
tweepyApi = tweepy.API(auth2)

# Authenticates tweepy API used
def Authenticate(CONSUMER_KEY_, CONSUMER_SECRET_):
    global CONSUMER_KEY
    global CONSUMER_SECRET

    CONSUMER_KEY = CONSUMER_KEY_
    CONSUMER_SECRET = CONSUMER_SECRET_

    global auth2
    global tweepyApi

    auth2 = tweepy.OAuthHandler(CONSUMER_KEY_, CONSUMER_SECRET_)
    tweepyApi = tweepy.API(auth2)

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
        return tweet['lang']

# Returns a single tweet's time stamp or a list of tweet's time stamps
def GetTweetTimeStamp(tweet):
    if(type(tweet) is list):
        timeStamps = []
        for singleTweet in tweet:
            timeStamps.append(GetTweetTimeStamp(singleTweet))
        return timeStamps
    else:
        return tweet['created_at']

# Returns a single tweet's author's name or a list of tweet's author's names
def GetTweetUserName(tweet):
    if(type(tweet) is list):
        timeStamps = []
        for singleTweet in tweet:
            timeStamps.append(GetTweetUserName(singleTweet))
        return timeStamps
    else:
        return tweet['user']['name']

# Returns a single tweet's author's user handle or a list of tweet's author's user handles
def GetTweetUserHandle(tweet):
    if(type(tweet) is list):
        timeStamps = []
        for singleTweet in tweet:
            timeStamps.append(GetTweetUserHandle(singleTweet))
        return timeStamps
    else:
        return tweet['user']['screen_name']

# Returns a single tweet's url or a list of tweet's urls
def GetTweetURL(tweet):
    if(type(tweet) is list):
        tweetURLs = []
        for singleTweet in tweet:
            tweetURLs.append(GetTweetURL(singleTweet))
        return tweetURLs
    else:
        return "https://twitter.com/username/status/" + tweet['id_str']

# Fully parses a single tweet or a list of tweets
def ParseTweet(tweet):
    if type(tweet) is list:
        parsedTweets = []
        for singleTweet in tweet:
            parsedTweets.append(ParseTweet(singleTweet))
        return parsedTweets
    else:
        parsedTweet = {}
        
        parsedTweet['text'] = GetTweetText(tweet)
        parsedTweet['lang'] = GetTweetLanguage(tweet)
        parsedTweet['time'] = GetTweetTimeStamp(tweet)
        parsedTweet['url'] = GetTweetURL(tweet)
        parsedTweet['name'] = GetTweetUserName(tweet)
        parsedTweet['handle'] = GetTweetUserHandle(tweet)
        parsedTweet['parsed'] = True

        return parsedTweet

# Returns a formatted string representing a parsed tweet
def GetParsedTweetString(tweet):
    string = ''

    string = string + tweet['name'] + ' (@' + tweet['handle'] + ')\n'
    string = string + '[' + tweet['time'] + '] \'' + tweet['lang'] + '\'\n-----\n'
    string = string + tweet['text'] + '\n-----\n'
    string = string + '{ ' + tweet['url'] + ' }'

    return string
