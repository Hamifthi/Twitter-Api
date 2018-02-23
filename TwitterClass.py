import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import API
import time

consumerKey = 'c16icxmBoqqhpZAMFZxlWNxYo'
consumerSecret = 'cW4Y6PbYfDVe15b6yeTQjWC9Og0kTOgpQt3caIEeLreasIRNeE'
accessToken = '967018015849148417-21nDpxdrdkAubl7NxFOZguy8Wr7o0Dd'
accessSecret = 'bfvCreJfsFb8ZjSjPViEGS9KSW13gWlYt4tRZYhg9OMij'

class Listner(StreamListener):

    def on_data(self, data):
        try:
            dataDict = json.loads(data)
            dataBase = open('tweetDB.txt', 'a', encoding = 'utf8')
            dataBase.write(dataDict['text'])
            dataBase.write('\n')
            dataBase.close()
            return True
        except BaseException as e:
            print(e)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)

twitterStream = Stream(auth, Listner())
twitterStream.filter(track = ['bitcoin'])