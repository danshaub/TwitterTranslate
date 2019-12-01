import twitter
import tweepy

authenticated = False

currentUsername = ''
signedIn = False

# Creates twitter api object
CONSUMER_KEY = 'N2j1JekR1RvkuPj5wKIBCgIm2'
CONSUMER_SECRET = '7IVq7i0SBdj5J43cVqcqYMlToPsxXN3Z86XkEZDPkSJbaqv4wC'
OAUTH_TOKEN = '979943818991616000-lDDZlHMnm42iGMNQvJih1nplvkun3xS'
OAUTH_TOKEN_SECRET = 'MIXdFMpRcs9uHKLw9HlP9JIJI5ZAXmCsjmJnIacFiVdFy'

# auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
# twitterApi = twitter.Twitter(auth=auth)
twitterApi = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=OAUTH_TOKEN, access_token_secret=OAUTH_TOKEN_SECRET)

auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
tweepyApi = tweepy.API(auth2)

def Authenticate(OAUTH_TOKEN_, OAUTH_TOKEN_SECRET_, CONSUMER_KEY_, CONSUMER_SECRET_):
    global CONSUMER_KEY
    global CONSUMER_SECRET
    global OAUTH_TOKEN
    global OAUTH_TOKEN_SECRET

    CONSUMER_KEY = CONSUMER_KEY_
    CONSUMER_SECRET = CONSUMER_SECRET_
    OAUTH_TOKEN = OAUTH_TOKEN_
    OAUTH_TOKEN_SECRET = OAUTH_TOKEN_SECRET_

    # global auth
    global twitterApi

    global auth2
    global tweepyApi

    # auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitterApi = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=OAUTH_TOKEN, access_token_secret=OAUTH_TOKEN_SECRET)

    auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    tweepyApi = tweepy.API(auth2)
    
    global authenticated
    authenticated = True

#searchResults = twitterApi.search.tweets(q=term, count=count, lang='en')

def Search(term, count, lang):
    print(authenticated)
    if not authenticated:
        raise Exception('Twitter Api not authenticated')

    search = twitterApi.search.tweets(q=term, count=count, lang=lang, result_type='recent')
    print(str(len(search['statuses'])) + " in Search")
    return search

def SignIn(username, num):
    # if not authenticated:
    #     raise Exception('Twitter Api not authenticated')

    global signedIn
    signedIn = True

    global currentUsername
    currentUsername = username

    tweetField = twitterApi.GetUserTimeline(screen_name=username, count=num)

    field_tweets = [i.AsDict() for i in tweetField]
    num = 1
    for t in field_tweets:
        print(num, ": ", t['id'], t['text'])
        num += 1

    #TODO: use twitter api to sign in to be able to view feed
    #TODO: raise exception if username is invalid

def ViewNextTweetInFeed():
    if not authenticated:
        raise Exception('Twitter Api not authenticated')

    if not signedIn:
        raise Exception('User not signed in')

    #TODO: return the next tweet of the feed

def RefreshFeed():
    if not authenticated:
        raise Exception('Twitter Api not authenticated')

    if not signedIn:
        raise Exception('User not signed in')

    #TODO: refresh ViewNextTweetInFeed() to give the first tweet in feed on next function call

    
