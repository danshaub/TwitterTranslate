# Author:  Dan Haub
# Chapman Email:  haub@chapman.edu
# Author:  Peter Chen
# Chapman Email:  haichen@chapman.edu
# Author:  Vincent Jodjana
# Chapman Email:  jodjana@chapman.edu
# Course Number and Section:  CPSC 353-02

# Twitter Translate [Main.py]

# The purpose of Main.py is to serve as the driver
# script for Twitter Translate

import sys
import codecs
import json
import os
from TwitterTranslate import TranslationHandler
from TwitterTranslate import TwitterHandler
from TwitterTranslate import TweetParser
from TwitterTranslate import SentimentAnalysis

#Sets output encoding
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Gathers Twitter Auth codes from file
dir = os.path.dirname(__file__)
# filename = os.path.join(dir, 'TwitterTranslate/files/TwitterAuth.txt')
filename = 'TwitterTranslate/Files/TwitterAuth.txt'
twitterAuth = open(filename, "r")
lines = []
for line in twitterAuth:
    lines.append(line.strip())

CONSUMER_KEY = str(lines[0][lines[0].index(': ')+2:])
CONSUMER_SECRET = str(lines[1][lines[1].index(': ')+2:])
OAUTH_TOKEN = str(lines[2][lines[2].index(': ')+2:])
OAUTH_TOKEN_SECRET = str(lines[3][lines[3].index(': ')+2:])

#Authenticates Twitter APIs
TwitterHandler.Authenticate(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

TweetParser.Authenticate(CONSUMER_KEY, CONSUMER_SECRET)

# List of statements used in the program
programStatements = ["Runing sentiment analysis",  # 0
                     "What is the search term?",  # 1
                     "How many languages would you like to test?",  # 2
                     "Invalid Response, please try again",  # 3
                     "Valid language codes are:",  # 4
                     "Chinese",  # 5
                     "English",  # 6
                     "French",  # 7
                     "Gernam",  # 8
                     "Italian",  # 9
                     "Japanese",  # 10
                     "Korean",  # 11
                     "Portuguese",  # 12
                     "Spanish",  # 13
                     "Input a language code",  # 14
                     "Invalid Language Code: Duplicated code",  # 15
                     "Invalid Language Code: Invalid Language or bad string",  # 16
                     "How many tweets per language?",  # 17
                     "Invalid Number of tweets",  # 18
                     "Starting Sentiment Analysis",  # 19
                     "Searching",  # 20
                     "Done",  # 21
                     "Parsing",  # 22
                     "Calculating Sentiment",  # 23
                     "Please enter a User Handle",  # 24
                     "Invalid handle, please try again",  # 25
                     "Display Language Codes?",  # 26
                     "Yes",  # 27
                     "No",  # 28
                     "Invalid language code, please try again",  # 29
                     "No more tweets",  # 30
                     "View another tweet",  # 31
                     "Refresh Feed",  # 32
                     "Change User",  # 33
                     "Change Language",  # 34
                     "view available languages",  # 35
                     "Return Home",  # 36
                     "Welcome to Twitter Translate!",  # 37
                     "What would you like to do?",  # 38
                     "Perform Sentiment Analysis",  # 39
                     "View Translated Twitter User Timeline",  # 40
                     "Exit",  # 41
                     "Exiting...",  # 42
                     "Peform another action?"] #43

#Translates program statements into OS language
programStatementsTrans = []

for statement in programStatements:
    programStatementsTrans.append(TranslationHandler.TranslateToSystemLang('en', statement))

#Translates language names into OS language
translatedLanguages = {}
for key in TranslationHandler.langNames:
    transLang = TranslationHandler.TranslateToSystemLang('en', TranslationHandler.langNames[key])
    translatedLanguages[key] = transLang

#Sentiment Analysis
def sentimentAnalysys():
    print(programStatementsTrans[0], flush=True)
    print()

    #Gahters search term
    searchTerm = input(programStatementsTrans[1] + "\n: ")
    print()

    #Detects the language of the search term
    termLang = TranslationHandler.DetectLanguage(searchTerm)

    numLanguages = ""
    validInput = False

    #Gathers number of languages to run sentiment analysis for
    while(not validInput):
        print(programStatementsTrans[2] + "(1 - 5)")
        numLanguages = input(": ")
        print()
        try:
            numLanguages = int(numLanguages)
        except:
            numLanguages = 0

        if((0 < numLanguages <= 5)):
            validInput = True
        else:
            print(programStatementsTrans[3])

    #Gahters language codes

    print(programStatementsTrans[4])
    print("\t" + programStatementsTrans[5] + ":  zh")
    print("\t" + programStatementsTrans[6] + ":  en")
    print("\t" + programStatementsTrans[7] + ":  fr")
    print("\t" + programStatementsTrans[8] + ":  de")
    print("\t" + programStatementsTrans[9] + ":  it")
    print("\t" + programStatementsTrans[10] + ":  ja")
    print("\t" + programStatementsTrans[11] + ":  ko")
    print("\t" + programStatementsTrans[12] + ":  pt")
    print("\t" + programStatementsTrans[13] + ":  es")

    print()

    validCodes = ['zh', 'en', 'fr', 'de', 'it', 'ja', 'ko', 'pt', 'es']


    langCodes = []
    index = 0
    while(index < numLanguages):
        validInput = False

        #Protects input to ensure no duplicate or invalid languages
        while(not validInput):
            code = input(programStatementsTrans[14] + "\n: ")
            print()
            if(langCodes.__contains__(code)):
                print(programStatementsTrans[15])
            elif(validCodes.__contains__(code)):
                validInput = True
                langCodes.append(code)
            else:
                print(programStatementsTrans[16])

        index = index+1

    #Gathers num tweets per language
    #TODO: Input protection (max 225 tweets total)
    numTweets = 0

    validInput = False
    while(not validInput):
        numTweets = input(programStatementsTrans[17] + "(1 - " + str(225//numLanguages) + ")\n: ")
        print()
        try:
            numTweets = int(numTweets)
        except:
            numTweets = 0

        if(0 < numTweets < (225//numLanguages)):
            validInput = True
        else:
            print(programStatementsTrans[18], flush=True)

    print(programStatementsTrans[19], flush=True)

    tweetSearches = []

    #Performs searches for each language
    for lang in langCodes:
        print(programStatementsTrans[20] + ": " + translatedLanguages[lang], flush=True)
        translatedTerm = ""
        
        #Translates search term into each language
        if lang == 'zh':
            translatedTerm = TranslationHandler.Translate(termLang, 'zh-TW', searchTerm)
            try:
                translatedTerm = translatedTerm.text
            except:
                translatedTerm = translatedTerm
        else:
            translatedTerm = TranslationHandler.Translate(termLang, lang, searchTerm)
            try:
                translatedTerm = translatedTerm.text
            except:
                translatedTerm = translatedTerm

        tweetSearches.append(TwitterHandler.Search(translatedTerm, numTweets, lang))

    print(programStatementsTrans[21], flush=True)
    print()

    #Parses tweets for text only
    tweetTexts = []
    index = 0
    for search in tweetSearches:

        print(programStatementsTrans[22] + ": " +
              translatedLanguages[langCodes[index]], flush=True)
        tweetTexts.append(TweetParser.GetTweetText(search))
        index = index + 1

    print(programStatementsTrans[21], flush=True)
    print()

    scores = []

    #Calculates average sentiment scores for each lanugage search
    index = 0
    for language in tweetTexts:
        print(programStatementsTrans[23] + ": " + translatedLanguages[langCodes[index]], flush=True)
        scores.append(SentimentAnalysis.SentimentScore(language))
        index = index + 1

    print(programStatementsTrans[21], flush=True)
    print()
    #prints language scores
    index = 0
    for score in scores:
        print(translatedLanguages[langCodes[index]] + ":  " + str(score), flush=True)
        index = index + 1

    print()
    return

#Chooses a twitter user to display tweets for
def PickUser():
    print(programStatementsTrans[24])
    handle = input(': ')

    #Makes sure the twitter user is valid
    while(not TwitterHandler.SignIn(handle)):
        print(programStatementsTrans[25])
        handle = input(': ')

#Chooses a language to display tweets in
def PickLanguage():
    validResponse = False

    #Allows user to display valid languages with input protection
    while(not validResponse):
        print(programStatementsTrans[26])
        print("1 - " + programStatementsTrans[27])
        print("2 - " + programStatementsTrans[28])

        response = input(": ")

        if response == "1":
            print()
            validResponse = True
            DisplayLanguages()
            print()
        elif response == "2":
            validResponse = True
            print()
        else:
            validResponse = False
            print(programStatementsTrans[3])

    codes = list(translatedLanguages.keys())

    #Allows user to enter a language code, proctects against invalid strings
    validResponse = False
    while(not validResponse):
        print(programStatementsTrans[14])
        response = input(": ")

        if (response == ' ') or not (response in codes):
            validResponse = False
            print(programStatementsTrans[29])
            print()
        else:
            validResponse = True
            return response

# Displays available languages in a clean format
def DisplayLanguages():
    # Determines the longest language name.
    longestLength = 0
    for key in translatedLanguages:
        if(len(translatedLanguages[key]) > longestLength):
            longestLength = len(translatedLanguages[key])

    # Makes an even number length list of language codes
    codes = list(translatedLanguages.keys())
    lengthOfCodes = len(codes)
    if(lengthOfCodes % 2 != 0):
        codes.append('-')
        translatedLanguages['-'] = '-'
        lengthOfCodes = lengthOfCodes + 1


    index1 = 0
    index2 = (lengthOfCodes//2) - 1

    #Displays language names and codes in two columns
    while(index2 < lengthOfCodes):
        print("{1:-<{0}}-  {2:5}  | {3:-<{0}}-  {4:5}".format(longestLength,
                                                          translatedLanguages[codes[index1]], codes[index1],
                                                          translatedLanguages[codes[index2]], codes[index2]))
        index1 = index1 + 1
        index2 = index2 + 1

#Prints the next tweet in a user feed translated to desired language
def GetNextTweet(lang):
    tweet = TwitterHandler.ViewNextTweetInFeed()
    tweetType = str(type(tweet))

    # Makes sure the tweet exists
    if(tweetType == '<class \'dict\'>'):
        tweet = TweetParser.ParseTweet(tweet)

        if(lang != tweet['lang'] and tweet['lang'] != 'und'):
            tweet['text'] = TranslationHandler.Translate(tweet['lang'], lang, tweet['text'])

        tweet = TweetParser.GetParsedTweetString(tweet)

        print('####################')
        print(tweet, flush=True)
        print('####################')
    
    # Otherwise shows that no more tweets are available
    else:
        print('####################')
        print(programStatementsTrans[30], flush=True)
        print('####################')

    return

# Returns the User Timeline to the newest tweet
def RefreshFeed():
    TwitterHandler.RefreshFeed()

# Allows user to view tweets made by a given twitter user
def viewTweets():
    lang = PickLanguage()
    print()

    PickUser()
    print()

    # Displays the first 5 tweets of the given twitter user
    GetNextTweet(lang)
    GetNextTweet(lang)
    GetNextTweet(lang)
    GetNextTweet(lang)
    GetNextTweet(lang)
    print()

    validResponse = False

    # Gives the user options on what to do next
    while(True):
        print('1- ' + programStatementsTrans[31])
        print('2- ' + programStatementsTrans[32])
        print('3- ' + programStatementsTrans[33])
        print('4- ' + programStatementsTrans[34])
        print('5- ' + programStatementsTrans[35])
        print('6- ' + programStatementsTrans[36])
        response = input(": ")

        # Displays another tweet
        if response == "1" or response == "":
            print()
            GetNextTweet(lang)
            print()
        # Refreshes twitter feed
        elif response == "2":
            RefreshFeed()
            print('\n' + programStatementsTrans[21] + '\n')
        # Chooses a new user
        elif response == "3":
            print()
            PickUser()
            RefreshFeed()
            print()
        # Chooses a new language
        elif response == "4":
            print()
            lang = PickLanguage()
            print()
        # Displays valid languages
        elif response == "5":
            print()
            DisplayLanguages()
            print()
        # Returns to main menu
        elif response == "6":
            return
        else:
            print(programStatementsTrans[3])

print()
print(programStatementsTrans[37])

#Program loop
while(True):
    validResponse = False

    # Shows main menu
    while(not validResponse):
        print()
        print(programStatementsTrans[38])
        print("1 - " + programStatementsTrans[39])
        print("2 - " + programStatementsTrans[40])
        print("3 - " + programStatementsTrans[41])

        response = input(": ")

        # Perform sentiment analysis
        if response == "1":
            print()
            validResponse = True
            sentimentAnalysys()
        # View twitter feeds
        elif response == "2":
            print()
            validResponse = True
            viewTweets()
        # Exit the program
        elif response == "3":
            print()
            validResponse = True
            print(programStatementsTrans[42])
            exit()
        else:
            validResponse = False
            print(programStatementsTrans[3])

    validResponse = False

    # Ask if user wants to do something else
    while(not validResponse):
        print()
        print(programStatementsTrans[43])
        print("1 - " + programStatementsTrans[27])
        print("2 - " + programStatementsTrans[28])

        response = input(": ")

        if response == "1":
            validResponse = True
        elif response == "2":
            validResponse = True
            print('Exiting...')
            exit()
        else:
            validResponse = False
            print(programStatementsTrans[3])
