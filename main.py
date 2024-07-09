# main.py
import tweepy
import pandas as pd
import json
from authorize import get_access_token

# Load Twitter API keys and tokens
with open("twitter_keys.json") as infile:
    json_obj = json.load(infile)
    bearer_token = json_obj["bearer_token"]

# Get OAuth 2.0 access token
access_token = get_access_token()
if access_token:
    print(f"Access Token: {access_token}")
else:
    print("Access Token Empty")

# Authenticate to Twitter using Bearer Token for API v2
client = tweepy.Client(bearer_token=bearer_token, access_token=access_token)

# Define the search term
search_term = "Tesla"

# Fetch tweets containing the search term using API v2
query = f"{search_term} lang:en -is:retweet"
tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at', 'id', 'text', 'public_metrics', 'lang'], max_results=100)

# Extract tweet information
tweet_data = []
if tweets.data:
    for tweet in tweets.data:
        tweet_info = {
            "Created_At": tweet.created_at,
            "Tweet_ID": tweet.id,
            "Text": tweet.text,
            "Retweet_Count": tweet.public_metrics['retweet_count'],
            "Favorite_Count": tweet.public_metrics['like_count'],
            "Language": tweet.lang
        }
        tweet_data.append(tweet_info)

# Create a DataFrame
df = pd.DataFrame(tweet_data)

# Save to Excel
file_path = "data/tesla_info.xlsx"
df.to_excel(file_path, index=False)

print(f"Data saved to {file_path}")
