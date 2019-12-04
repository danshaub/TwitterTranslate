# Author:  Dan Haub
# Chapman Email:  haub@chapman.edu
# Author:  Peter Chen
# Chapman Email:  haichen@chapman.edu
# Author:  Vincent Jodjana
# Chapman Email:  jodjana@chapman.edu
# Course Number and Section:  CPSC 353-02

# Twitter Translate [TwitterHandler.py]

# The purpose of TwitterHandler.py is to serve as a
# wrapper module for the twitter and tweepy APIs

import twitter
import tweepy

authenticated = False

currentUsername = ''
currentTweetID = 0
signedIn = False

# Creates twitter api object
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitterApi = twitter.Twitter(auth=auth)

auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
tweepyApi = tweepy.API(auth2)

# Authenticates twitter and tweepy API wrappers
def Authenticate(OAUTH_TOKEN_, OAUTH_TOKEN_SECRET_, CONSUMER_KEY_, CONSUMER_SECRET_):
    global CONSUMER_KEY
    global CONSUMER_SECRET
    global OAUTH_TOKEN
    global OAUTH_TOKEN_SECRET

    CONSUMER_KEY = CONSUMER_KEY_
    CONSUMER_SECRET = CONSUMER_SECRET_
    OAUTH_TOKEN = OAUTH_TOKEN_
    OAUTH_TOKEN_SECRET = OAUTH_TOKEN_SECRET_

    global auth
    global twitterApi

    global auth2
    global tweepyApi

    # Authenticates twitter package
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitterApi = twitter.Twitter(auth=auth)

    # Authenticates tweepy package
    auth2 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    tweepyApi = tweepy.API(auth2)
    
    global authenticated
    authenticated = True

# Searches for tweets given a term, a language, and a count
def Search(term, count, lang):
    if not authenticated:
        raise Exception('Twitter Api not authenticated')

    # Performs initial search
    search = twitterApi.search.tweets(q=term, count=count, lang=lang, result_type='recent')
    statuses = search['statuses']

    # Ensures the correct number of tweets are found
    for _ in range(9):
        try:
            next_results = search['search_metadata']['next_results']
        # except KeyError, e:  # No more results when next_results doesn't exist
        except KeyError:
            break

        # Create a dictionary from next_results, which has the following form:
        # ?max_id=313519052523986943&q=NCAA&include_entities=1
        kwargs1 = dict([kv.split('=') for kv in next_results[1:].split("&")])

        search_results1 = twitterApi.search.tweets(**kwargs1)
        statuses += search_results1['statuses']

    return statuses

# Chooses and verifies the validity of a twitter handle to display tweets from
def SignIn(username):
    if not authenticated:
        raise Exception('Twitter Api not authenticated')
    
    # Attempts to collect the first tweet from a user, catches an exception otherwise
    try:
        tweetField = twitterApi.statuses.user_timeline(screen_name=username, count=1)

        if(username != tweetField[0]['user']['screen_name']):
            raise "Bad username"
        
        global currentTweetID
        currentTweetID = tweetField[0]['id']
        
        global signedIn
        signedIn = True

        global currentUsername
        currentUsername = username

        # Returns true if the sign in is successful
        return True

    except:
        # Returns false if the sign in is unsuccessful
        return False

# Returns the next tweet for the specified user
def ViewNextTweetInFeed():
    if not authenticated:
        raise Exception('Twitter Api not authenticated')

    if not signedIn:
        raise Exception('User not signed in')
    
    global currentTweetID
    global currentUsername

    tweetField = twitterApi.statuses.user_timeline(screen_name=currentUsername, count=1, max_id=currentTweetID)
    
    try:
        # Sets next tweet ID to be older than the current tweet
        currentTweetID = tweetField[0]['id'] - 1

        return tweetField[0]
    except:
        # if no more tweets exist, returns null
        return

# Returns the current tweet ID to the most recent tweet on a user's timeline
def RefreshFeed():
    if not authenticated:
        raise Exception('Twitter Api not authenticated')

    if not signedIn:
        raise Exception('User not signed in')

    global currentTweetID
    global currentUsername

    tweetField = twitterApi.statuses.user_timeline(screen_name=currentUsername, count=1)

    global currentTweetID
    currentTweetID = tweetField[0]['id']
