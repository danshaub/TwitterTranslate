import twitter
import tweepy

authenticated = False

currentUsername = ''
signedIn = False

# Creates twitter api object
CONSUMER_KEY = 'jUFNTGtGfD4UrxHejpXikiygr'
CONSUMER_SECRET = 'Pa5lv6grtNisg8FBQPEDlUs9jqcFdDCCDqc2ueneNxCMMNdFuH'
OAUTH_TOKEN = '979943818991616000-Q4yuhGWthAI4fN1DDKFrLCgCNyFbgRZ'
OAUTH_TOKEN_SECRET = 'z6TjmSQMg2Lc0sEnX9iZnsLbZyESxKncEjeULx4qcI0W0'

# auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
# twitterApi = twitter.Twitter(auth=auth)
twitterApi = twitter.Api(consumer_key=CONSUMER_KEY,
                         consumer_secret=CONSUMER_SECRET,
                         access_token_key=OAUTH_TOKEN,
                         access_token_secret=OAUTH_TOKEN_SECRET)

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
    # twitterApi = twitter.Twitter(auth=auth)
    twitterApi = twitter.Api(consumer_key=CONSUMER_KEY,
                             consumer_secret=CONSUMER_SECRET,
                             access_token_key=OAUTH_TOKEN,
                             access_token_secret=OAUTH_TOKEN_SECRET)

    auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    tweepyApi = tweepy.API(auth2)
    
    global authenticated
    authenticated = True

#searchResults = twitterApi.search.tweets(q=term, count=count, lang='en')

def Search(term, count, lang):
    # if not authenticated:
    #     raise Exception('Twitter Api not authenticated')


    search = twitterApi.GetSearch(term=term, count=count, lang=lang, result_type='recent')
    # print(str(len(search['statuses'])) + " in Search")
    for tweet in search:
        print(tweet.id, tweet.text)
    return search
# =======
#     search = twitterApi.search.tweets(q=term, count=count, lang=lang, result_type='recent')
#     statuses = search['statuses']


#     for _ in range(9):
#         try:
#             next_results = search['search_metadata']['next_results']
#         # except KeyError, e:  # No more results when next_results doesn't exist
#         except KeyError:
#             break

#         # Create a dictionary from next_results, which has the following form:
#         # ?max_id=313519052523986943&q=NCAA&include_entities=1
#         kwargs1 = dict([kv.split('=') for kv in next_results[1:].split("&")])

#         search_results1 = twitterApi.search.tweets(**kwargs1)
#         statuses += search_results1['statuses']

#     return statuses
# >>>>>>> eddd2570d6b57c9378c36fe65a7e23f77547bdfb

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

    
