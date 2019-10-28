import twitter
import sys
import codecs
import json


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q1 = input('Enter a search term: ')

search_results = twitter_api.search.tweets(q=q1, count=5)

search_json = json.dumps(search_results, indent=4)

print(search_json)

input()
