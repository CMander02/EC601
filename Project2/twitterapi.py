# Copyright 2022 Ziyan Chen zychen02@bu.edu
import tweepy
import wordcloud

# Put your Bearer Token in the parenthesis below
client = tweepy.Client(
    bearer_token='AAAAAAAAAAAAAAAAAAAAAFcahwEAAAAAMFceIP9bTucYDtQEjoZiCMxDGXE%3DwHpnFVugad6KK6GzEAPyGBT83fGqo0DK5WJX4ojzsjSTad5Usf'
)

# Get information of a account
name = input("Please enter the username you want to fetch: ")
account_info = client.get_users(
    usernames=name,
    user_fields=[
        "public_metrics,description,profile_image_url,verified,protected,location,url"
    ],
)

for user in account_info.data:
    print("Name: ", user.name)
    print("Username: ", user.username)
    print("ID: ", user.id)
    print("Profile Image URL: ", user.profile_image_url)
    print("Description: ", user.description)
    print("Verified: ", user.verified)
    print("Location: ", user.location)
    print("URL: ", user.url)
    print("\n")

# Get recent tweets on a certain hashtag
query = input("Please enter the hashtag(without #) you want to search: ")
max = input("Please enter the number of results you want to represent(10~100): ")

query += ' -is:retweet lang:en'
tweets = client.search_recent_tweets(
    query=query, tweet_fields=['context_annotations', 'created_at'], max_results=max
)

# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english
# For more annotations, go to
# https://developer.twitter.com/en/docs/twitter-api/annotations/overview

recent_tweet_text = ""
num = 0
for tweet in tweets.data:
    num += 1
    print("NO.", num)
    print(tweet.text)
    recent_tweet_text += tweet.text
    print("\n")

# Generate Word Cloud
w = wordcloud.WordCloud(
    width=1000, height=1000, background_color='white', max_words=100
)
w.generate(recent_tweet_text)
w.to_file('wordcloud.png')
