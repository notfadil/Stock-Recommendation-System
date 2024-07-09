import tweepy

# Replace 'your_bearer_token' with your actual bearer token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOnAugEAAAAAhbPf1mkuU7zzhvF3bSyslqWX0VU%3Dl2yZU6txUwMMohOeWatwzAYKnHt0fT0goQcnzpezbe9HMLajNB"

# Initialize the OAuth2 Bearer Token handler
auth = tweepy.OAuth2BearerHandler(bearer_token)

# Create the API object
api = tweepy.API(auth)

# Example: Fetching public tweets
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
