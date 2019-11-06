import twitter
import sys
import codecs
import json
from googletrans import Translator

import TweetParse

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

translator = Translator()

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitterApi = twitter.Twitter(auth=auth)

term = input("enter a search term in english:  ")
langCode = input("enter a language code:  ")
count = input("enter a number of tweets:  ")

translatedTerm = translator.translate(term, dest=langCode).text

print("translated search term: " + translatedTerm)

searchResults = twitterApi.search.tweets(q=term, count=count, lang='en')
translatedSearchResults = twitterApi.search.tweets(q=translatedTerm, count=count, lang=langCode)

tweetsEnglish = searchResults['statuses']
tweetsOther = translatedSearchResults['statuses']

textsEnglish = TweetParse.GetTweetText(tweetsEnglish)
textsOther = TweetParse.GetTweetText(tweetsOther)

count = 1
for text in textsEnglish:
    print(""+ str(count) + ":  " + text)
    count = count + 1

print("\n\n Other Language \n*****************\n")

count = 1
for text in textsOther:
    print("" + str(count) + ":  " + text)
    count = count + 1
