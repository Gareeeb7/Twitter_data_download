import tweepy
import re
import pickle
import numpy as np

from tweepy import OAuthHandler

# Initializing the keys

consumer_key = '8OnSqCr8V25GJU1NlBTqtcAXD'
consumer_secret = 'YGhc2cQyPhImUFhZfx1EuWUjQVFxTxYn7dWSSBbmprSFA9U0Hf'
access_token = '908129063520288768-bqhFZk4fjCywy0mYpLr7yEiLwXPiJ8r'
access_secret = 'x0wrFwQ6dKp5TaQlhuNQhLLOBnmTMTvaDrAGIzu11oyci'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

args = ['#lockdown']
api = tweepy.API(auth,timeout=10)


list_tweets = []

query = args[0]
if len(args) == 1:
    for status in tweepy.Cursor(api.search,q=query+"-filter:tweets",lang='en',result_type='recent').items(3000):
        list_tweets.append(status.text)


import pandas as pd

df = pd.DataFrame(list_tweets)
df.to_csv('C:/Users/user/.spyder-py3/range/Lockdown.csv',index=False)





#preproccessing
'''       
for tweets in list_tweets:
    tweets = re.sub(r"^ "," ",tweet)
    tweets = re.sub(r"^ "," ",tweet)
    tweets = re.sub(r"^ "," ",tweet)
    tweet = tweet.lower
    tweets = re.sub(r"^ "," ",tweet)
    tweets = re.sub(r"^ "," ",tweet)
    tweets = re.sub(r"^ "," ",tweet)
    tweets = re.sub(r"^ "," ",tweet)
    
print(tweet)
    '''
    
    
    
    
    
