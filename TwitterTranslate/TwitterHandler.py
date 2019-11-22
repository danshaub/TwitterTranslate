import twitter
from TwitterTranslate import TweetParser
from TwitterTranslate import TranslationHandler


# Creates twitter api object
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitterApi = twitter.Twitter(auth=auth)

parser = TweetParser

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitterApi = twitter.Twitter(auth=auth)

#searchResults = twitterApi.search.tweets(q=term, count=count, lang='en')

def Search(term, count, lang):
    return twitterApi.search.tweets(q=term, count=count, lang='en')

# def SignIn(username, password)
