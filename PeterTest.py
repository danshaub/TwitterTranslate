import tweepy
import twitter
import sys
import codecs
import json
<<<<<<< HEAD
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

print(TweetParser.GetTweetText(TwitterHandler.ViewNextTweetInFeed()))
print()
print(TweetParser.GetTweetText(TwitterHandler.ViewNextTweetInFeed()))
print()
print(TweetParser.GetTweetText(TwitterHandler.ViewNextTweetInFeed()))
print()
print(TweetParser.GetTweetText(TwitterHandler.ViewNextTweetInFeed()))
print()
print(TweetParser.GetTweetText(TwitterHandler.ViewNextTweetInFeed()))
print()

print("\n\n")
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
TwitterHandler.RefreshFeed()

print(TweetParser.GetTweetText(TwitterHandler.ViewNextTweetInFeed()))
print()
print(TweetParser.GetTweetText(TwitterHandler.ViewNextTweetInFeed()))
print()
print(TweetParser.GetTweetText(TwitterHandler.ViewNextTweetInFeed()))
print()
print(TweetParser.GetTweetText(TwitterHandler.ViewNextTweetInFeed()))
print()
print(TweetParser.GetTweetText(TwitterHandler.ViewNextTweetInFeed()))
print()

# texts = []

# for tweet in tweets:
#     texts.append(TweetParser.ParseTweet(tweet))

# count = 1

# for text in texts:
#     print(str(count) + ": " + str(text))
#     count = count + 1
=======
# from googletrans import Translator
# from TwitterTranslate import TranslationHandler
# from TwitterTranslate import TwitterHandler
# from TwitterTranslate import TweetParser
# from TwitterTranslate import SentimentAnalysis
# from tkinter import *
# import TwitterTranslate.TranslationHandler
import TwitterTranslate.TwitterHandler
# import TwitterTranslate.TweetParser
# import TwitterTranslate.SentimentAnalysis

# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# translationHandler = TranslationHandler
# twitterHandler = TwitterHandler
# tweetParser = TweetParser
# sentimentAnalysis = SentimentAnalysis
# translator = Translator()

# # Creates twitter api object
# CONSUMER_KEY = ''
# CONSUMER_SECRET = ''
# OAUTH_TOKEN = ''
# OAUTH_TOKEN_SECRET = ''

# twitterHandler.Authenticate(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# tweetParser.Authenticate(CONSUMER_KEY, CONSUMER_SECRET)
CONSUMER_KEY = 'jUFNTGtGfD4UrxHejpXikiygr'
CONSUMER_SECRET = 'Pa5lv6grtNisg8FBQPEDlUs9jqcFdDCCDqc2ueneNxCMMNdFuH'
OAUTH_TOKEN = '979943818991616000-Q4yuhGWthAI4fN1DDKFrLCgCNyFbgRZ'
OAUTH_TOKEN_SECRET = 'z6TjmSQMg2Lc0sEnX9iZnsLbZyESxKncEjeULx4qcI0W0'

# auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
# twitterApi = twitter.Twitter(auth=auth)

#TwitterTranslate.TwitterHandler.Authenticate(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
TwitterTranslate.TwitterHandler.Authenticate(
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
TwitterTranslate.TwitterHandler.SignIn("ElonMuskNewsOrg", 10)
TwitterTranslate.TwitterHandler.Search("hello", 5, "en")
>>>>>>> b33d697d224971c7c7efeb3b2e4779b0a2b8c89f
