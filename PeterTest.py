import tweepy
import twitter
import sys
import codecs
import json
import os
from googletrans import Translator
from TwitterTranslate import TranslationHandler
from TwitterTranslate import TwitterHandler
from TwitterTranslate import TweetParser
from TwitterTranslate import SentimentAnalysis
from tkinter import *

# Sets output encoding
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

translator = Translator()

# Gathers Twitter Auth codes from file
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'TwitterTranslate/files/TwitterAuth.txt')

twitterAuth = open(filename, "r")
lines = []
for line in twitterAuth:
    lines.append(line.strip())

CONSUMER_KEY = str(lines[0][lines[0].index(': ')+2:])
CONSUMER_SECRET = str(lines[1][lines[1].index(': ')+2:])
OAUTH_TOKEN = str(lines[2][lines[2].index(': ')+2:])
OAUTH_TOKEN_SECRET = str(lines[3][lines[3].index(': ')+2:])

# Authenticates Twitter APIs
TwitterHandler.Authenticate(
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

TweetParser.Authenticate(CONSUMER_KEY, CONSUMER_SECRET)

TwitterHandler.SignIn("ElonMuskNewsOrg")

print(TweetParser.GetParsedTweetString(TweetParser.ParseTweet(TwitterHandler.ViewNextTweetInFeed())))
print()
print(TweetParser.GetParsedTweetString(TweetParser.ParseTweet(TwitterHandler.ViewNextTweetInFeed())))
print()
print(TweetParser.GetParsedTweetString(TweetParser.ParseTweet(TwitterHandler.ViewNextTweetInFeed())))
print()
print(TweetParser.GetParsedTweetString(TweetParser.ParseTweet(TwitterHandler.ViewNextTweetInFeed())))
print()
print(TweetParser.GetParsedTweetString(TweetParser.ParseTweet(TwitterHandler.ViewNextTweetInFeed())))
print()

print("\n\n")
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
TwitterHandler.RefreshFeed()

print(TweetParser.GetParsedTweetString(TweetParser.ParseTweet(TwitterHandler.ViewNextTweetInFeed())))
print()
print(TweetParser.GetParsedTweetString(TweetParser.ParseTweet(TwitterHandler.ViewNextTweetInFeed())))
print()
print(TweetParser.GetParsedTweetString(TweetParser.ParseTweet(TwitterHandler.ViewNextTweetInFeed())))
print()
print(TweetParser.GetParsedTweetString(TweetParser.ParseTweet(TwitterHandler.ViewNextTweetInFeed())))
print()
print(TweetParser.GetParsedTweetString(TweetParser.ParseTweet(TwitterHandler.ViewNextTweetInFeed())))
print()

# texts = []

# for tweet in tweets:
#     texts.append(TweetParser.ParseTweet(tweet))

# count = 1

# for text in texts:
#     print(str(count) + ": " + str(text))
#     count = count + 1
