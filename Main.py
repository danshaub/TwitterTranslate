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
from tkinter import *

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

translationHandler = TranslationHandler
twitterHandler = TwitterHandler
tweetParser = TweetParser
sentimentAnalysis = SentimentAnalysis
translator = Translator()

# Creates twitter api object
CONSUMER_KEY = 'N2j1JekR1RvkuPj5wKIBCgIm2'
CONSUMER_SECRET = '7IVq7i0SBdj5J43cVqcqYMlToPsxXN3Z86XkEZDPkSJbaqv4wC'
OAUTH_TOKEN = '979943818991616000-lDDZlHMnm42iGMNQvJih1nplvkun3xS'
OAUTH_TOKEN_SECRET = 'MIXdFMpRcs9uHKLw9HlP9JIJI5ZAXmCsjmJnIacFiVdFy'

twitterHandler.Authenticate(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

tweetParser.Authenticate(CONSUMER_KEY, CONSUMER_SECRET)

'''

result = TwitterHandler.Search('dog', 4, 'en')
statuses = result['statuses']
texts = TweetParser.ParseTweet(statuses)

print(json.dumps(result, indent=4))

count = 1
for text in texts:
    print(str(count) + ":  " + str(text))
    print()
    count = count+1
'''

'''
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
root.mainloop()
'''
