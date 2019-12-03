###############################################################
# Written by Dan Haub in November 2019                        #
#                                                             #
# The purpose of Main.py is to serve as the core program file #
# for twitter translate.                                      #
###############################################################

import sys
import codecs
import json
import os
from TwitterTranslate import TranslationHandler
from TwitterTranslate import TwitterHandler
from TwitterTranslate import TweetParser
from TwitterTranslate import SentimentAnalysis
from googletrans import Translator
translator = Translator()

#Sets output encoding
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

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

#Authenticates Twitter APIs
TwitterHandler.Authenticate(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

TweetParser.Authenticate(CONSUMER_KEY, CONSUMER_SECRET)

word = translator.translate(text='안녕하세요.', src='ko', dest='ja')
print(word)


# List of statements used in the program
programStatements = ["Welcome to Twitter Translate!", # 0
                     "What would you like to do?", # 1 
                     "Perform Sentiment Analysis", # 2
                     "View Translated Twitter User Timeline", # 3
                     "Exit", # 4
                     "Invalid Response, please try again", # 5
                     "Exiting...", # 6
                     "Peform another action?", # 7
                     "yes", # 8
                     "no", # 9
                     "Runing sentiment analysis", # 10
                     "How many languages would you like to test?", # 11
                     "Input a language code", # 12
                     "View Language Codes", # 13
                     "How many tweets per language?", # 14
                     "What is the search term?", # 15
                     "Invalid number of tweets", # 16
                     "Chinese", # 17
                     "English", # 18
                     "French", # 19
                     "German", # 20
                     "Italian", # 21
                     "Japanese", # 22
                     "Korean", # 23
                     "Portuguese", # 24
                     "Spanish", # 25
                     "Valid language codes are:", # 26
                     "Invalid Language Code: Invalid Language or bad string", # 27
                     "Invalid Language Code: Duplicated code", # 28
                     "Invalid Number of tweets", # 29
                     "Searching", # 30
                     "Parsing", # 31
                     "Calculating Sentiment", # 32
                     "Done", # 33
                     "Starting Sentiment Analysis"] 

#Translates program statements into OS language
programStatementsTrans = []

for statement in programStatements:
    programStatementsTrans.append(TranslationHandler.TranslateToSystemLang(statement))

translatedLanguages = {}
for key in TranslationHandler.langNames:
    transLang = TranslationHandler.TranslateToSystemLang(TranslationHandler.langNames[key])
    translatedLanguages[key] = transLang

print(translatedLanguages)

#Sentiment Analysis
def sentimentAnalysys():
    print(programStatementsTrans[10])
    print()

    #Gahters search term
    searchTerm = input(programStatementsTrans[15] + "\n: ")
    print()

    termLang = TranslationHandler.DetectLanguage(searchTerm)

    numLanguages = ""
    validInput = False

    #Gathers number of languages to run sentiment analysis for
    while(not validInput):
        print(programStatementsTrans[11] + "(1 - 5)")
        numLanguages = input(": ")
        print()
        try:
            numLanguages = int(numLanguages)
        except:
            numLanguages = 0
        
        if((0 < numLanguages <= 5)):
            validInput = True
        else:
            print(programStatementsTrans[5])

    #Gahters language codes
    #TODO: Input protection

    print(programStatementsTrans[26])
    print("\t" + programStatementsTrans[17] + ":  zh")
    print("\t" + programStatementsTrans[18] + ":  en")
    print("\t" + programStatementsTrans[19] + ":  fr")
    print("\t" + programStatementsTrans[20] + ":  de")
    print("\t" + programStatementsTrans[21] + ":  it")
    print("\t" + programStatementsTrans[22] + ":  ja")
    print("\t" + programStatementsTrans[23] + ":  ko")
    print("\t" + programStatementsTrans[24] + ":  pt")
    print("\t" + programStatementsTrans[25] + ":  es")

    print()

    validCodes = ['zh', 'en', 'fr', 'de', 'it', 'ja', 'ko', 'pt', 'es']

    langCodes = []
    index = 0
    while(index < numLanguages):
        validInput = False

        while(not validInput):
            code = input(programStatementsTrans[12] + "\n: ")
            print()
            if(langCodes.__contains__(code)):
                print(programStatementsTrans[28])
            elif(validCodes.__contains__(code)):
                validInput = True
                langCodes.append(code)
            else:
                print(programStatementsTrans[27])
            
        index = index+1
    
    #Gathers num tweets per language
    #TODO: Input protection (max 225 tweets total)
    numTweets = 0
    
    validInput = False
    while(not validInput):
        numTweets = input(programStatementsTrans[14] + "(1 - " + str(225//numLanguages) + ")\n: ")
        print()
        try:
            numTweets = int(numTweets)
        except:
            numTweets = 0
        
        if(0 < numTweets < (225//numLanguages)):
            validInput = True
        else:
            print(programStatementsTrans[29])

    print(programStatementsTrans[34])
    
    tweetSearches = []

    #Performs searches for each language
    for lang in langCodes:
        print(programStatementsTrans[30] + ": " + translatedLanguages[lang])
        translatedTerm = ""

        if lang == 'zh':
            translatedTerm = TranslationHandler.Translate(termLang, 'zh-TW', searchTerm).text
        else:
            translatedTerm = TranslationHandler.Translate(termLang, lang, searchTerm).text

        tweetSearches.append(TwitterHandler.Search(translatedTerm, numTweets, lang))
    
    print(programStatementsTrans[33])
    print()

    #Parses tweets for text only
    tweetTexts = []
    index = 0
    for search in tweetSearches:
        print(programStatementsTrans[31] + ": " + translatedLanguages[langCodes[index]])
        tweetTexts.append(TweetParser.GetTweetText(search))
        index = index + 1

    print(programStatementsTrans[33])
    print()

    scores = []

    #Calculates average sentiment scores for each lanugage search
    index = 0
    for language in tweetTexts:
        print(programStatementsTrans[32] + ": " + translatedLanguages[langCodes[index]])
        scores.append(SentimentAnalysis.SentimentScore(language))
        index = index + 1

    print(programStatementsTrans[33])
    print()
    #prints language scores
    index = 0
    for score in scores:
        print(translatedLanguages[langCodes[index]] + ":  " + str(score))
        index = index + 1

    print()
    return

#TwitterFeed
def viewTweets():
    print(TranslationHandler.TranslateToSystemLang("Error: Feature does not exist"))
    return

print(programStatementsTrans[0])

#Program loop
while(True):
    validResponse = False

    while(not validResponse):
        print()
        print(programStatementsTrans[1])
        print("1 - " + programStatementsTrans[2])
        print("2 - " + programStatementsTrans[3])
        print("3 - " + programStatementsTrans[4])

        response = input(": ")

        if response == "1":
            print()
            validResponse = True
            sentimentAnalysys()
        elif response == "2":
            print()
            validResponse = True
            viewTweets()
        elif response == "3":
            print()
            validResponse = True
            print(programStatementsTrans[6])
            exit()
        else:
            validResponse = False
            print(programStatementsTrans[5])
    
    validResponse = False

    while(not validResponse):
        print()
        print(programStatementsTrans[7])
        print("1 - " + programStatementsTrans[8])
        print("2 - " + programStatementsTrans[9])

        response = input(": ")

        if response == "1":
            validResponse = True
        elif response == "2":
            validResponse = True
            print(programStatementsTrans[6])
            exit()
        else:
            validResponse = False
            print(programStatementsTrans[5])
