import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

keyword = input("Enter keyword to search: ")

query = f'{keyword} -is:retweet'

response = client.search_recent_tweets(query=query, max_results=26, tweet_fields=["created_at", "lang", "public_metrics"])

tweets = []
for i, tweet in enumerate(response.data):
    if i == 25: 
        print("There are more than 25 tweets")
        break
    tweets.append(tweet.text)

