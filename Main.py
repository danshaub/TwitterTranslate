###############################################################
# Written by Dan Haub in November 2019                        #
#                                                             #
# The purpose of Main.py is to serve as the core program file #
# for twitter translate.                                      #
###############################################################


import tweepy
import twitter
import sys
import codecs
import json
from googletrans import Translator
from TwitterTranslate import TranslationHandler
from TwitterTranslate import TwitterHandler
from TwitterTranslate import TweetParser
from TwitterTranslate import SentimentAnalysis
from tkinter import Tk, Label, Button

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
"""
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text=TranslationHandler.Translate("en", "fr", "Welcome to twitter translate!").text)
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop() """

# Creates translator object
translator = Translator()

# Creates parser object
parser = TweetParser

# Creates twitter api object
CONSUMER_KEY = 'gKkxTnXxqn3v3tFjrfu9oZeYB'
CONSUMER_SECRET = 'HDomCUoqsy933LKptgRtMcNtOzo0UaY3ML8OGmiV375mdL1NNH'
OAUTH_TOKEN = '702034289-1w5CFub2H5ZR7EOol3OWyb2Yq6NQrFjACos7gr6O'
OAUTH_TOKEN_SECRET = '5EXFQg8vIaL6xBr6YTsoewvxjwa7Z9QL36daBfP0OLJcz'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

# auth for tweppy library
auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# set up the tweepy twitter api
twitterApi = twitter.Twitter(auth=auth)
tweepyApi = tweepy.API(auth2)

# Collects user input
term = input(TranslationHandler.TranslateToSystemLang("enter a search term:  "))
langCode = input(TranslationHandler.TranslateToSystemLang("enter a language code:  "))
count = input(TranslationHandler.TranslateToSystemLang("enter a number of tweets:  "))

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
textsEnglish = parser.GetTweetText(tweetsEnglish, tweepyApi)
textsOther = parser.GetTweetText(tweetsOther, tweepyApi)

# Prints english texts
for text in textsEnglish:
    temp = {'text':text}

    print(""+ str(SentimentAnalysis.SentimentScore(temp)) + ":  " + str(text))

print("\n\n Other Language \n*****************\n")

# Prints other language texts

for text in textsOther:
    temp = {'text':text}

    print(""+ str(SentimentAnalysis.SentimentScore(temp)) + ":  " + str(text))
