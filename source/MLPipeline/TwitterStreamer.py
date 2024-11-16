

# from tweepy import Stream
import time

from .TwitterAuth import TwitterAuth
from .TweetsListener import TweetsListener
from .References import References

import requests
import time
class TwitterStreamer(References):
    """Class to handle fetching recent tweets and sending to Kafka."""

    def __init__(self, producer):
        self.twitterAuth = TwitterAuth()
        self.producer = producer
        self.listener = TweetsListener(producer, self.TOPIC_NAME)
        self.last_tweet_id = None  # Store the ID of the last fetched tweet
        
        # Twitter recent search API endpoint
        self.search_url = "https://api.twitter.com/2/tweets/search/recent"
        
    def fetch_recent_tweets(self):
        """Fetch recent tweets based on the configured query parameters."""
        query_params = {
            "query": self.TRACK_TWEET,
            "expansions": "author_id",
            "tweet.fields": "created_at,lang",
            "user.fields": "username",
            "max_results": 10  # Number of tweets to retrieve per request
        }
        if self.last_tweet_id:
            query_params["since_id"] = self.last_tweet_id
        
        headers = {
            "Authorization": f"Bearer {self.twitterAuth.bearer_token}",
            "User-Agent": "v2TweetSearch"
        }

        response = requests.get(self.search_url, headers=headers, params=query_params)
        
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return []
        # Process response JSON
        data = response.json().get("data", [])
        users = response.json().get("includes", {}).get("users", [])

        # Create a dictionary to map user ID to user details (name and username)
        user_map = {user['id']: user for user in users}

        # Iterate over the tweet data and add user info (name, username) to each tweet
        for tweet in data:
            author_id = tweet.get("author_id")
            user_info = user_map.get(author_id, {})
            tweet["author_name"] = user_info.get("name", "Unknown")  # Display name
            tweet["author_username"] = user_info.get("username", "Unknown")  # Username        
        return data

    def stream_tweets(self):
        """Fetch and process tweets in a loop, simulating a continuous stream."""
        while True:
            try:
                tweets = self.fetch_recent_tweets()
                
                for tweet_data in tweets:
                    self.listener.process_tweet(tweet_data)
                
                time.sleep(10)  # Wait for 30 seconds before fetching again

                if tweets:
                    self.last_tweet_id = tweets[0]["id"]
            except Exception as e:
                print("Error fetching tweets:", e)
                time.sleep(5)  # Wait before retrying

