import tweepy
import twitter
import sys
import codecs
import json
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
CONSUMER_KEY = 'N2j1JekR1RvkuPj5wKIBCgIm2'
CONSUMER_SECRET = '7IVq7i0SBdj5J43cVqcqYMlToPsxXN3Z86XkEZDPkSJbaqv4wC'
OAUTH_TOKEN = '979943818991616000-lDDZlHMnm42iGMNQvJih1nplvkun3xS'
OAUTH_TOKEN_SECRET = 'MIXdFMpRcs9uHKLw9HlP9JIJI5ZAXmCsjmJnIacFiVdFy'

# auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
# twitterApi = twitter.Twitter(auth=auth)

#TwitterTranslate.TwitterHandler.Authenticate(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
TwitterTranslate.TwitterHandler.SignIn("ElonMuskNewsOrg", 10)
TwitterTranslate.TwitterHandler.Authenticate(
    CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
TwitterTranslate.TwitterHandler.Search("hello", 5, "en")
