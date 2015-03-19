#!usr/bin/python3.4

import json

tweet_dict = []
tweets = open('20150305_08.out', 'r')
for line in tweets:
    try:
        tweet_dict.append(json.loads(line))
    except ValueError as errorMessage:
        print ('Tweet parse error: "'+ str(errorMessage) + '"', file=sys.stderr)
    print(tweet_dict)
