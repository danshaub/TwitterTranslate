import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


#ParsedTweet{text: "string", lang: "string"}
#tweet = {'text': "hello world", 'lang': "en"}
#print(tweet['text'])
#print(tweet['lang'])

def print_result(annotations)
    score = annotations.document_sentiment.score

    for index, sentence in enumerate(annotations.sentences) :
            sentence_sentiment = sentence.sentiment.score
            print('Sentence {} has a sentimnet score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {}'.format(score))
    return 0

def analyze(tweet):
    #Runs a sentiment analysis request
    client = language.LanguageServiceClient()

    with open(tweet, 't') as user_tweet:
        content = tweet.read()

    print_result(annotations)

if name == 'main':
    parser = argparse.ArgumentParser(
        description=doc,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        'tweet',
        help='The tweet you would like to analyze.')

    args = parser.parse_args()

    analyze(args.tweet)
