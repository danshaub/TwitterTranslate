import twitter
import sys
import codecs
import json


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

CONSUMER_KEY = 'gKkxTnXxqn3v3tFjrfu9oZeYB'
CONSUMER_SECRET = 'HDomCUoqsy933LKptgRtMcNtOzo0UaY3ML8OGmiV375mdL1NNH'
OAUTH_TOKEN = '702034289-1w5CFub2H5ZR7EOol3OWyb2Yq6NQrFjACos7gr6O'
OAUTH_TOKEN_SECRET = '5EXFQg8vIaL6xBr6YTsoewvxjwa7Z9QL36daBfP0OLJcz'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

q1 = input('Enter a search term: ')

search_results = twitter_api.search.tweets(q=q1, count=5)

search_json = json.dumps(search_results, indent=4)

print(search_json)

input()