# TwitterTranslate

Twitter Translate is a Twitter client that provides tools for sentiment analysis and feed viewing that are centered around language translation. Twitter Translate can:

* detect the language of the operating system and translate all program messages accordingly,
* compare sentiment on a given search term across up to five languages at a time,
* display a twitter user's feed in one of 101 different languages, and
* provide a link to each tweet displayed from a user feed

Twitter Translate accomplishes this through the use of Python3.7, Google's Natural Language API, and Twitter's Developer API

## Required Files (place in "Files" directory)

* GoogleAuth.json
  * Google generated API Key json file
* TwitterAuth.txt
  * Twitter API keys formatted as follows:
    * CONSUMER_KEY: [Key Value]
    * CONSUMER_SECRET: [Key Value]
    * OAUTH_TOKEN: [Key Value]
    * OAUTH_TOKEN_SECRET: [Key Value]

## Program Instructions

* clone github repo
* place GoogleAuth.json and TwitterAuth.txt into TwitterTranslate/TwitterTranslate/Files
* cd into TwitterTranslate directory
* run: "docker build -t twitter_translate:latest ."
* run: "docker run -it twitter_translate"

### Known Issues

* When run from a docker image, Twitter Translate is unable to detect system language and defaults to English
* The googletrans python package sometimes fails to translate, Twitter Translate displays a message when this failure occurs
