#ParsedTweet{text: "string", lang: "string"}
#print(tweet['text'])
#print(tweet['lang'])
#analyze(tweet)

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
print("Enter a tweet to analyze: ")
tweet = input()
language = "en"
#tweet = {'text': "hello world", 'lang': "en"}
document = types.Document(
    content=tweet,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Tweet: {}'.format(tweet))
print('Language: {}'.format(language))
print('Sentiment: {}'.format(sentiment.score))
