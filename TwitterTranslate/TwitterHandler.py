import twitter
from TwitterTranslate import TweetParser
from TwitterTranslate import TranslationHandler

translator = TranslationHandler
parser = TweetParser

# Creates twitter api object
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitterApi = twitter.Twitter(auth=auth)
