import tweepy
import json
import configData
from tweepy import OAuthHandler

consumer_key = configData.CONSUMER_KEY
consumer_secret = configData.CONSUMER_SECRET
access_token = configData.ACCESS_TOKEN
access_secret = configData.ACCESS_SECRET

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def process_or_store(tweet):
    print(json.dumps(tweet))

#for status in tweepy.Cursor(api.home_timeline).items(1):
    # Process a single status
#    print(status.text)

# List all followers
#for friend in tweepy.Cursor(api.friends).items():
#	process_or_store(friend._json)

# List all my tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)