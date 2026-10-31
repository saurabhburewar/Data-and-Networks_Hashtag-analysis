#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:42:14 2021

@author: ritu
"""

import tweepy
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# assign the values accordingly
#consumer_key = ""
#consumer_secret = ""
#access_token = ""
#access_token_secret = ""

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth, wait_on_rate_limit=True)


df=pd.read_csv('tweet_id_by_hashtag.csv',usecols=['or_id'])
#file = open("graph_twitter_retweet.csv", "w")
#file.write(str(123))
#file.write(str(235))
H= nx.Graph()


db = pd.DataFrame(columns=['username','following', 'followers', 'totaltweets', 'retweetcount', 'retweeters'])
#print(df)
i=1
for t_id in df['or_id']:
    try:
        or_status=api.get_status(t_id)
        or_username=or_status.user.screen_name
        or_following=or_status.user.friends_count
        or_followers=or_status.user.followers_count
        or_totaltweets=or_status.user.statuses_count
        or_retweetcount=or_status.retweet_count
        H.add_node(or_username)
        retweets_list = api.retweets(t_id)
        print("tweet number:", i)
        # print(t_id, or_username, or_following, or_followers, or_totaltweets, or_retweetcount)
        retweeter_list=[]
        for retweet in retweets_list:
            retweeter_list.append(retweet.user.screen_name)
            H.add_edge(or_username, retweet.user.screen_name)
        ith_tweet = [or_username, or_following, or_followers, or_totaltweets, or_retweetcount, retweeter_list]
        db.loc[len(db)] = ith_tweet
        # print(retweeter_list)
        i=i+1
    except Exception:
        print("Exception occured")
        continue
nx.write_edgelist(H, "graph_edgelist.csv",delimiter=',')
print()
# print("H",H)


filename = 'blacklivesmatter_master.csv'
db.to_csv(filename)

fig = plt.figure(1, figsize=(200, 100), dpi=60)
nx.draw(H)
plt.savefig("filename1.png")

G=nx.read_edgelist("graph_edgelist.csv",delimiter=',')

print(G.number_of_nodes())
# n
