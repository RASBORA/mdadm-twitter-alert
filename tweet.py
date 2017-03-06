#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Tweepyライブラリをインポート
import tweepy
import sys

CONSUMER_KEY = '7J5zlGbq8ksp7TnPRGVcl0eGk'
CONSUMER_SECRET = 'XojN3JUsoD3c7N0CBVxvNA7eKk5vJmMpgO7N2muLVZoy4dZkD0'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

for arg in sys.argv:


api.update_status(status=text)
