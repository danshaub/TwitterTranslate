###############################################################
# Written by Dan Haub in November 2019                        #
#                                                             #
#                                                             #
###############################################################

from googletrans import Translator
import os


def GetSystemLanguage():
    return os.getenv('LANG')

def Translate(fromLang, toLang, message):
    translator = Translator()
    return translator.translate(text=message, src=fromLang, dest=toLang)

# def Translate(toLang, text):
#     return Translate("en", toLang, text)

def GetWelcomeMessage():
    message = "Welcome to Twitter Translate!\n"
    if(GetSystemLanguage() == "en"):
        return message
    else:
        return Translate(fromLang="en", toLang=GetSystemLanguage(), message=message).text


translator = Translator()
print(GetWelcomeMessage())
print(translator.translate(text="Hello World", dest=GetSystemLanguage()))
