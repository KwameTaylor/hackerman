import tweepy
import json

path = "../generator/"

from keys import *

import sys
sys.path.append(path)
import hackergenerator

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweet = hackergenerator.sentence();

api.update_status(status = tweet)
