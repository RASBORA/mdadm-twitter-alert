#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tweepy
import sys
import os.path

CONSUMER_KEY = 'bHvXbznxDz0UhaKz7q1BHetOY'
CONSUMER_SECRET = 'tC5RNt2d9lLW9PT9M2qVyi8kz28U2fRyVBI3oKfRarodUU0GuC'

app_path = os.path.dirname(os.path.abspath(__file__))

ACCESS_TOKEN = open(os.path.join(app_path,'ACCESS_TOKEN'), 'r').read()
ACCESS_SECRET = open(os.path.join(app_path,'ACCESS_SECRET'), 'r').read()

# Authorize
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Create tweet
TWEET_HEADER = u'' # example: u'@user'
TWEET_FOOTER = u'#Alert'

text = TWEET_HEADER + u' \n'
for arg in sys.argv[1:]:
    text += arg + u'\n'

text += TWEET_FOOTER

# Send tweet
api.update_status(status=text)
