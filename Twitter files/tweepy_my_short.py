#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 04:51:34 2021

@author: ritu
"""


import pandas as pd
import tweepy

#def printtweetdata(n, ith_tweet):
#    print()
#    print(f"Tweet {n}:")
#    print(f"Username:{ith_tweet[0]}")
#    print(f"Description:{ith_tweet[1]}")
#    print(f"Location:{ith_tweet[2]}")
#    print(f"Following Count:{ith_tweet[3]}")
#    print(f"Follower Count:{ith_tweet[4]}")
#    print(f"Total Tweets:{ith_tweet[5]}")
#    print(f"Retweet Count:{ith_tweet[6]}")
#    print(f"Tweet Text:{ith_tweet[7]}")
#    print(f"Hashtags Used:{ith_tweet[8]}")
    
def printshort(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"id: {ith_tweet[0]}")

def scrape(words, date_since, numtweet):
    try:  
        # Creating DataFrame using pandas
    #    db1 = pd.DataFrame(columns=['username', 'description', 'location', 'following',
    #                               'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags','tweet_id'])
    #    db2 =  pd.DataFrame(columns=['tweet_id', 'or_id','username', 'following', 'followers', 'totaltweets', 'retweetcount']) 
        db =  pd.DataFrame(columns=['or_id']) 
    
        # We are using .Cursor() to search through twitter for the required tweets.
        # The number of tweets can be restricted using .items(number of tweets)
        tweets = tweepy.Cursor(api.search, q=words, lang="en", since=date_since, tweet_mode='extended').items(numtweet)
         
        # .Cursor() returns an iterable object. Each item in 
        # the iterator has various attributes that you can access to 
        # get information about each tweet
        list_tweets = [tweet for tweet in tweets]
          
        # Counter to maintain Tweet Count
        i = 1  
          
        # we will iterate over each tweet in the list for extracting information about each tweet
        for tweet in list_tweets:
    #        if i==2:
    #        print(tweet)
    #        or_id=None
            originaltweetid=None
            try:
                if(tweet.retweeted_status):
                    originalTweet = tweet.retweeted_status;
        #            print("Or_stat",originalTweet)
                    originaltweetid = originalTweet.id;
                    or_id=originaltweetid
    #                or_status=api.get_status(or_id)
    #                or_username=or_status.user.screen_name
    #                or_following=or_status.user.friends_count
    #                or_followers=or_status.user.followers_count
    #                or_totaltweets=or_status.user.statuses_count
    #                or_retweetcount=or_status.user.retweet_count
        #            if(originaltweetid==tweet.id):
        #                continue
        #            continue
        #            originaluserid = originalTweet.getUser().getId();
            except AttributeError:
                print("AttributeError")
            t_id = tweet.id
            or_id=originaltweetid
            
    #        username = tweet.user.screen_name
    #        description = tweet.user.description
    #        location = tweet.user.location
    #        following = tweet.user.friends_count
    #        followers = tweet.user.followers_count
    #        totaltweets = tweet.user.statuses_count
    #        retweetcount = tweet.retweet_count
    #        hashtags = tweet.entities['hashtags']
            
    #        or_status=api.get_status(or_id)
    #        or_username=or_status.user.screen_name
    #        or_following=or_status.user.friends_count
    #        or_followers=or_status.user.followers_count
    #        or_totaltweets=or_status.user.statuses_count
    #        or_retweetcount=or_status.user.retweet_count
    #        print("or_username",or_username)
              
            # Retweets can be distinguished by a retweeted_status attribute,
            # in case it is an invalid reference, except block will be executed
            
    #        try:
    #            text = tweet.retweeted_status.full_text
    #        except AttributeError:
    #            text = tweet.full_text
    #        hashtext = list()
    #        followers_list = list()
    #        for j in range(0, len(hashtags)):
    #            hashtext.append(hashtags[j]['text'])
    #        for follower in api.followers(username):
    #            followers_list.append(follower.screen_name)
                
            # Here we are appending all the extracted information in the DataFrame
    #        ith_tweet1 = [username, description, location, following,
    #                     followers, totaltweets, retweetcount, text, hashtext, t_id]
    #        ith_tweet2 = [t_id,or_id, username, following, followers, totaltweets, retweetcount]
    #        ith_tweet2 = [or_id, or_username, or_following, or_followers, or_totaltweets, or_retweetcount]
            if(or_id==None):
                print("or_id==None")
                ith_tweet=[t_id]
            else:
                ith_tweet=[or_id]
            if ith_tweet not in db.values:
                db.loc[len(db)] = ith_tweet
                printshort(i, ith_tweet)
                i = i+1
            # Function call to print tweet data on screen
    #        printtweetdata(i, ith_tweet)
            
        filename = 'tweet_id_by_hashtag.csv'
          
        # we will save our database as a CSV file.
        db.to_csv(filename)
    except Exception:
        print("Exception Funct")
        pass
    
if __name__ == '__main__':
    try:
        # Enter your own credentials obtained 
        # from your developer account
        consumer_key = "Es6QTSTLrBR68Grq2RGCQHHzN"
        consumer_secret = "qrOpg2ZcQJjuwbRvjWFNMjGO6TFR4suC8H653E0ZOMcrZNlDhE"
        access_key = "1316092784156184576-AoldpvD7a7XfBD4bOoq8CqY1RPWlhu"
        access_secret = "lX475cmxFuEq5uE3Ffgt8ZjNFWouyqOxmJmFphb2imo4y"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
          
        # Enter Hashtag and initial date
    #    print("Enter Twitter HashTag to search for")
    #    words = input()
    #    print("Enter Date since The Tweets are required in yyyy-mm--dd")
    #    date_since = input()
        hashtag = "#viratkholi"
        since = "2021-01-01"
        # number of tweets you want to extract in one run
        numtweet = 2500
        scrape(hashtag, since, numtweet)
        print('Scraping has completed!')
    except Exception:
        print("Exception Main")
        pass
    
#