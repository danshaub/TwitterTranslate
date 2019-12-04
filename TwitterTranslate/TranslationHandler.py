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

# Finds language names and codes from file
dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'Files/languageCodes.txt')

# Constructs two dictionaries with codes and languages
langCodes = {}
langNames = {}

with open(filename) as f:
    for line in f:
        (lang, code) = line.split('**')
        if code.endswith('\n'):
            code = code[:-1]
        langCodes[lang] = code
        langNames[code] = lang

# Returns the language of the operating system
def GetSystemLanguage():
    if(os.getenv('LANG') == 'C.UTF8'):
        return 'en'
    else:
        return str(os.getenv('LANG').split(".")[0])

# Translates a string of text
def Translate(fromLang, toLang, message):
    # Ensures languages are different
    if(fromLang.startswith(toLang) or toLang.startswith(fromLang)):
        return message
    # If they are different, translate
    else:
        try:
            return translator.translate(text=message, src=fromLang, dest=toLang)
        except:
            print('**TRANSLATION NOT AVAILABLE**')
            return message

# Translates a string of text to the OS language
def TranslateToSystemLang(fromLang, message):
    translation = Translate(fromLang=fromLang, toLang=GetSystemLanguage(), message=message)

    try:
        translation = translation.text
        return translation
    except:
        return translation

# Detects the language of a string of text
def DetectLanguage(sampleSentence):
    try:
        return translator.detect(sampleSentence).lang
    except:
        return 'en'
