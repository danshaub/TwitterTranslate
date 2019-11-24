###############################################################
# Written by Dan Haub in November 2019                        #
#                                                             #
# The purpose of Main.py is to serve as the core program file #
# for twitter translate.                                      #
###############################################################

# using another library tweepy for twitter api
import tweepy
import twitter
import sys
import codecs
import twitter
import json
# import TwitterTranslate.TweetParser
import TweetParser

from googletrans import Translator

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Creates translator object
translator = Translator()

# Creates parser object
parser = TweetParser

# Creates twitter api object
CONSUMER_KEY = 'It4voosHW6TyL6iVjvzPiirqk'
CONSUMER_SECRET = 'f1fCFFwbz80qUxLpO155Btzn1HPV0N2fXgatZVLCPVAj7xoVE7'
OAUTH_TOKEN = '979943818991616000-i2OzeJ71Y288wBWrMlw6zJcRIlwD676'
OAUTH_TOKEN_SECRET = '4SADdllXvyPFyKur7eFrV3AfqaxffezU1F5tgKx2ikdzJ'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

# auth for tweppy library
auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# set up the tweepy twitter api
twitterApi = twitter.Twitter(auth=auth)
api = tweepy.API(auth2)

# Collects user input
term = input("enter a search term in english:  ")
langCode = input("enter a language code:  ")
count = input("enter a number of tweets:  ")

# Translates search term into other language
translatedTerm = translator.translate(term, dest=langCode).text

# Collects search qurerys from both english and other language
searchResults = twitterApi.search.tweets(
    q=term, count=count, lang='en')

translatedSearchResults = twitterApi.search.tweets(q=translatedTerm, count=count, lang=langCode)

# Collects the list of tweets from the query
tweetsEnglish = searchResults['statuses']
tweetsOther = translatedSearchResults['statuses']

# Collects tweet texts from the tweets
# textsEnglish = parser.GetTweetText(tweetsEnglish)
# textsOther = parser.GetTweetText(tweetsOther)

# Prints english texts
# count = 1
# for text in textsEnglish:
#     # print(""+ str(count) + ":  " + str(text))
#     # used another python library tweepy to get all the tweets
#     # in this library, we can modify the tweet_mode to extended, which allow us to get full length of tweets
#     status = api.get_status(str(text), tweet_mode="extended")
#     try:
#         print(str(count), ", ", status.retweeted_status.full_text)
#     except AttributeError:  # Not a Retweet
#         print(str(count), ", ", status.full_text)
#     count = count + 1

parser.GetTweetText(tweetsEnglish)

print("\n\n Other Language \n*****************\n")

# Prints other language texts
# count = 1
# for text in textsOther:
#     # print("" + str(count) + ":  " + str(text))
#     status = api.get_status(str(text), tweet_mode="extended")
#     try:
#         print(str(count), ", ", status.retweeted_status.full_text)
#     except AttributeError:  # Not a Retweet
#         print(str(count), ", ", status.full_text)
#     count = count + 1

parser.GetTweetText(tweetsOther)

