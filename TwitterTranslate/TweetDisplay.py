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

statuses = search_results['statuses']

for _ in range(5):
    try:
        next_results = search_results['search_metadata']['next_results']
    # except KeyError, e:  # No more results when next_results doesn't exist
    except KeyError:
        break

    # Create a dictionary from next_results, which has the following form:
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])

    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

# Show one sample search result by slicing the list...
# print(json.dumps(statuses[0], indent=1))

status_texts = [status['text']
                for status in statuses]

screen_names = [user_mention['screen_name']
                for status in statuses
                for user_mention in status['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in statuses
            for hashtag in status['entities']['hashtags']]

words = [w
         for t in status_texts
         for w in t.split()]

for i in range(0,5):
    print(json.dumps(status_texts[i], indent=1))
    print()
