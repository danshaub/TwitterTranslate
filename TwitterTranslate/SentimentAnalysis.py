#ParsedTweet{text: "string", lang: "string"}
#print(tweet['text'])
#print(tweet['lang'])
#analyze(tweet)

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from TwitterTranslate import TranslationHandler

#TranslationHandler.langCodes
#TranslationHandler.langNames

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
print("Enter a tweet to analyze: ")
tweet = input()
language = "en"
# tweet = {'text': "hello world", 'lang': "en"}
document = types.Document(
    content=tweet,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Tweet: {}'.format(tweet))
print('Language: {}'.format(language))
print('Sentiment: {}'.format(sentiment.score))

# Function Outline
def SetimentScore(tweet):
    if(type(tweet) is list):
        scores = []
        for singleTweet in tweet:
            scores.append(SetimentScore(singleTweet))
        return scores
    else:
        sentimentScore = 0

        # use tweet['text'] and tweet['lang'] to calculate a sentiment score

        return sentimentScore
