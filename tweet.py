#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tweepy
import sys

CONSUMER_KEY = '7J5zlGbq8ksp7TnPRGVcl0eGk'
CONSUMER_SECRET = 'XojN3JUsoD3c7N0CBVxvNA7eKk5vJmMpgO7N2muLVZoy4dZkD0'

TWEET_HEADER = u'' # example: u'@user'
TWEET_FOOTER = u''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

text = u'' + TWEET_HEADER + u'\n'
for arg in sys.argv:
    text += arg + u'\n'

text += TWEET_FOOTER

api.update_status(status=text)
