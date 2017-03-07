#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tweepy
import sys

CONSUMER_KEY = '7J5zlGbq8ksp7TnPRGVcl0eGk'
CONSUMER_SECRET = 'XojN3JUsoD3c7N0CBVxvNA7eKk5vJmMpgO7N2muLVZoy4dZkD0'

ACCESS_TOKEN = open('ACCESS_TOKEN', 'r').read()
ACCESS_SECRET = open('ACCESS_SECRET', 'r').read()

# Authorize
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Create tweet
TWEET_HEADER = u'' # example: u'@user'
TWEET_FOOTER = u''

text = TWEET_HEADER + u'\n'
for arg in sys.argv[1:]:
    text += arg + u'\n'

text += TWEET_FOOTER

# Send tweet
api.update_status(status=text)
