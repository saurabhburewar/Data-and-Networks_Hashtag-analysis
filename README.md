# Hashtag-analysis

High resolution images of the networks and more details available here -  
https://saurabhburewar.github.io/Data-and-Networks_Hashtag-analysis/

## Introduction

In this project, we have analyzed the social network formed by the users when they use a particular hashtag in a tweet on Twitter or post on Koo to understand how the network translates in the real world, and the social impact of a particular hashtag in the real world. This will be used to understand the network structure that is formed in the most popular hashtags. These hashtags are related to society and help us understand the online interaction that is necessary to make a hashtag/social cause successful online, using various social network analysis metrics.

## How to run scripts

All the code and data used for twitter is stored in the directory "Twitter files" and all the data and code for koo is stored in directory "koo".

### Twitter

Make sure to install the following python libraries -
- Tweepy
- Networkx
- Pandas
- Matplotlib

Follow these steps to run -
- Enter your Twiiter API key, API secret, access token and access token secret in the variables in the files "tweepy_my_short.py" and "create_network.py". 
- Change the 'hashtag', 'since' and 'numtweet' variables in "tweepy_my_short.py" to what you want and run the script.
```
python tweepy_my_short.py
```
- Once "tweet_id_by_hashtag.csv" is completed, run the "create_network.py" script to get the tweets and build a network. 
```
python create_network.py
```
- The data is stored in a csv file and an edgelist and PNG is stored for the graph.

### Koo

Make sure to install the following python libraries -
- Selenium
- Networkx
- Pandas

Follow these steps to run -
- Download the chromedriver for your version of chrome and make sure it is in the same directory.
- Change the URL in the driver.get() method in "rekoo.py" to the URL of the hashtag page you want to scrape.
- You can run the function "rekoo_net()" to build the rekoo network and "hash_net" to build hashtag-hashtag network.
- Run the script.
```
python rekoo.py
```
- The script saves the data in a csv file periodically, so you can stop the script in between. If not, it will keep scraping until it reaches the end of the webpage.
- Once you have the csv file containing the data, run "generate_net.py" to build the network.
```
python generate_net.py
```
- An edgelist and PNG is stored for the graph.

## Report

You can read the full report [here](https://github.com/saurabhburewar/Data-and-Networks_Hashtag-analysis/blob/main/Report/Hashtag%20Network%20Analysis%20report%20final.pdf).
