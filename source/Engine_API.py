
from flask import Flask, request

from MLPipeline.ReplyTweets import ReplyTweet
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods = ['POST','GET'])
@cross_origin()
def replyTweet():
    """ Reply to Tweets """
    print(request.form)
    data = request.form
    data={"tweet": "@AmericanAir is the most unprofessional airline on earth", "user": "_xDontMindMe", "tweet_id": "1407791710902571008"}
    reply = ReplyTweet()
    return reply.reply_toTweet(data['tweetId'], data['complain'], data['complain_type'], data['user'])

if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)

