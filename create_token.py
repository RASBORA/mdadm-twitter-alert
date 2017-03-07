#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tweepy
import webbrowser

CONSUMER_KEY = 'bHvXbznxDz0UhaKz7q1BHetOY'
CONSUMER_SECRET = 'tC5RNt2d9lLW9PT9M2qVyi8kz28U2fRyVBI3oKfRarodUU0GuC'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

redirect_url = auth.get_authorization_url()
print('Get your verification code from: ' + redirect_url)

webbrowser.open(redirect_url)
verifier = input('Type the verification code: ').strip()

auth.get_access_token(verifier)
ACCESS_TOKEN = auth.access_token
ACCESS_SECRET = auth.access_token_secret

with open("ACCESS_TOKEN","w") as fp:
    fp.write(ACCESS_TOKEN)
with open("ACCESS_SECRET","w") as fp:
    fp.write(ACCESS_SECRET)

# http://www.statsbeginner.net/entry/2015/10/21/131717
