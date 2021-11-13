#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 09:02:25 2021

@author: ritu
"""


import tweepy
import pandas as pd

  
# assign the values accordingly
#consumer_key = ""
#consumer_secret = ""
#access_token = ""
#access_token_secret = ""

consumer_key = "Es6QTSTLrBR68Grq2RGCQHHzN"
consumer_secret = "qrOpg2ZcQJjuwbRvjWFNMjGO6TFR4suC8H653E0ZOMcrZNlDhE"
access_token = "1316092784156184576-AoldpvD7a7XfBD4bOoq8CqY1RPWlhu"
access_token_secret = "lX475cmxFuEq5uE3Ffgt8ZjNFWouyqOxmJmFphb2imo4y"
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth, wait_on_rate_limit=True)
  
# the ID of the tweet
ID = 1265889240300257280
#ID = 1272479136133627905

ID = 1455236401071484929
#  
# getting the retweeters
retweets_list = api.retweets(ID)
status= api.get_status(ID)
#file= 'sample status.txt'
file = open("sample status.txt", "w")
file.write(str(status))
#print(status)
#print(retweets_list)
# printing the screen names of the retweeters
for retweet in retweets_list:
    print(retweet.user.screen_name)