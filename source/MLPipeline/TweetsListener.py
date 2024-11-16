import json

class TweetsListener:
    """Process fetched tweets and send them to Kafka."""

    def __init__(self, producer, topic_name):
        self.producer = producer
        self.topic_name = topic_name

    def process_tweet(self, tweet_data):
        """Process tweet data and send it to Kafka."""
        try:
            print(tweet_data)
            # Extract relevant fields
            tweet_text = tweet_data.get("text", "")
            tweet_id = tweet_data.get("id", "")
            author_name = tweet_data.get("author_username", "")
            
            # Prepare output data
            out_data = {
                "tweet": tweet_text.replace("\n", ""),
                "user": author_name,
                "tweet_id": tweet_id
            }
            print("Sending to Kafka:", out_data)
            
            # Send tweet data to Kafka topic
            self.producer.send(self.topic_name, json.dumps(out_data).encode('utf-8'))
        except Exception as e:
            print("Error processing tweet:", e)