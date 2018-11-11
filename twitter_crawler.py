import tweepy
import csv
import pandas as pd
# input your credentials here
consumer_key = 'h0CgjECj95JMCRrfAEM8NquDu'
consumer_secret = '5EZEqs3pUMx3elbR4k4Q6u6WtMQ3S9GSadtreyq2hXVy2DJ4Qp'
access_token = '2803200109-KXRu6pAniQeYkWcx6SHpuQGXIH46zldGBStWbGi'
access_token_secret = 'NEVN9BQOG6XEDmmzPdbpjMSh7BzaI290qg6QZLjupPmXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

csvFile = open('lol.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q="pvpstejos",
                           tweet_mode="extended").items():
    print (tweet.created_at, tweet.full_text)
    csvWriter.writerow(
        [tweet.created_at, tweet.full_text.encode('ascii', errors='ignore')])
