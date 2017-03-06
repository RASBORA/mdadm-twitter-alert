#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tweepy
import webbrowser
import time
import platform
import json

from pprint import pprint

CONSUMER_KEY = '7J5zlGbq8ksp7TnPRGVcl0eGk'
CONSUMER_SECRET = 'XojN3JUsoD3c7N0CBVxvNA7eKk5vJmMpgO7N2muLVZoy4dZkD0'

redirect_url = auth.get_authorization_url()
print 'Get your verification code from: ' + redirect_url

webbrowser.open(redirect_url)
verifier = raw_input('Type the verification code: ').strip()

auth.get_access_token(verifier)
ACCESS_TOKEN = auth.access_token
ACCESS_SECRET = auth.access_token_secret

ACCESS_TOKEN_HANDLE     = open("ACCESS_TOKEN","w")
ACCESS_SECRET_HANDLE    = open("ACCESS_SECRET","w")
ACCESS_TOKEN_HANDLE.write(ACCESS_TOKEN)
ACCESS_SECRET_HANDLE.write(ACCESS_SECRET)

# http://www.statsbeginner.net/entry/2015/10/21/131717
