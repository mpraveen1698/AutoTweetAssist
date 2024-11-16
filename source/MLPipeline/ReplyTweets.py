
# Send Tweets from twitter API
#Import necessary packages
import json
import random
import requests
from requests_oauthlib import OAuth1
from .References import References

class ReplyTweet(References):

    def __init__(self):
        # Use OAuth1 for write access
        self.auth = OAuth1(
            self.consumer_key,
            self.consumer_secret,
            self.access_token,
            self.access_token_secret
        )

        # Twitter API endpoint for posting a tweet (API v2)
        self.url = "https://api.twitter.com/2/tweets"

    def sendReply(self, tweetId, user, text):
        try:
            # Prepend username to the reply text
            reply_text = f"@{user} {text}"

            # Data for the reply
            payload = {
                "text": reply_text,
                "reply": {
                    "in_reply_to_tweet_id": tweetId
                }
            }

            # Send POST request to create a reply
            response = requests.post(self.url, json=payload, auth=self.auth)

            # Check the response
            if response.status_code == 201:
                print("Reply posted successfully:", response.json())
                return True
            else:
                print("Failed to post reply:", response.status_code, response.json())
                return False

        except Exception as e:
            print("An error occurred:", e)
            return False
    
    def getReplyText(self, complain_type, ticketId):
        reply_txt = f"""We apologize for the inconvenience caused. Your issue has been logged under ticket ID: {ticketId}.
Our team is working to resolve it. For any further assistance, contact:
- Email: support@proj.com
- Phone: +1 (123) 456-7890
Thank you."""

        return reply_txt

    def reply_toTweet(self, tweetId, complain, complain_type, user):
        if bool(complain):
            ticketId = int(random.random() * 100000)
            txt = self.getReplyText(complain_type, ticketId)
            replied = self.sendReply(tweetId, user, txt)
        else:
            ticketId = ""
            replied = False
        return json.dumps({"replied": replied, "ticketId": ticketId})

