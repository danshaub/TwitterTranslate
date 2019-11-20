###############################################################
# Written by Dan Haub in November 2019                        #
#                                                             #
# The purpose of TranslantionHandler.py is to provide         #
# functions to easily detect language, translate to specified #
# languages and handle the System Language. Also provides     #
# dictionaries for converting between language codes and      #
# language names                                              #
###############################################################

from googletrans import Translator
import os

translator = Translator()

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '..\SentimentScoreLibraries\languageCodes.txt')

langCodes = {}
langNames = {}

with open(filename) as f:
    for line in f:
        (lang, code) = line.split()
        langCodes[lang] = code
        langNames[code] = lang

def GetSystemLanguage():
    return str(os.getenv('LANG').split(".")[0])

def Translate(fromLang, toLang, message):
    return translator.translate(text=message, src=fromLang, dest=toLang)

def TranslateToSystemLang(message):
    return Translate(fromLang=translator.detect(message).lang, toLang=GetSystemLanguage(), message=message).text

def DetectLanguage(sampleSentence):
    return translator.detect(sampleSentence)

print(GetSystemLanguage())
print(TranslateToSystemLang("Welcome to Twitter Translate!\n What would you like to do?"))

sentence = input(TranslateToSystemLang("Type a sentence in any language"))

print(DetectLanguage(sentence))
print(TranslateToSystemLang(sentence))



