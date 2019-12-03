# Author:  Dan Haub
# Chapman Email:  haub@chapman.edu
# Author:  Peter Chen
# Chapman Email:  haichen@chapman.edu
# Author:  Vincent Jodjana
# Chapman Email:  jodjana@chapman.edu
# Course Number and Section:  CPSC 353-02

# Twitter Translate [TranslationHandler.py]

# The purpose of TranslantionHandler.py is to provide
# functions to easily detect language, translate to specified
# languages and handle the System Language. Also provides
# dictionaries for converting between language codes and
# language names

from googletrans import Translator
import os

translator = Translator()

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'files/languageCodes.txt')

langCodes = {}
langNames = {}

with open(filename) as f:
    for line in f:
        (lang, code) = line.split('**')
        if code.endswith('\n'):
            code = code[:-1]
        langCodes[lang] = code
        langNames[code] = lang

def GetSystemLanguage():
    return str(os.getenv('LANG').split(".")[0])

def Translate(fromLang, toLang, message):
    if(fromLang.startswith(toLang) or toLang.startswith(fromLang)):
        return message
    else:
        try:
            return translator.translate(text=message, src=fromLang, dest=toLang)
        except:
            print('**TRANSLATION NOT AVAILABLE**')
            return message

def TranslateToSystemLang(fromLang, message):
    translation = Translate(fromLang=fromLang, toLang=GetSystemLanguage(), message=message)

    try:
        translation = translation.text
        return translation
    except:
        return translation

def DetectLanguage(sampleSentence):
    try:
        return translator.detect(sampleSentence).lang
    except:
        return 'en'
