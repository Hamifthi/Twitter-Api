import DataBase
import tweepy
class Listner(tweepy.StreamListener):

    def on_data(self, data):
        try:
            return data
        except:
            print(error)

    def on_error(self, status):
        print(status)

class Twitter:
    def __init__ (self, consumerKey, consumerSecret, accessToken, accessSecret):
        self.consumerKey = consumerKey
        self.consumerSecret = consumerSecret
        self.accessToken = accessToken
        self.accessSecret = accessSecret
        self.auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        self.auth.set_access_token(self.accessToken, self.accessSecret)
        self.api = tweepy.API(self.auth)
        self.DataBase = DataBase.DataBase()
        self.listner = Listner()

    def search (self, objectName, object):
        self.DataBase.save(objectName, self.api.search(str(object) if type(object) != list else object))
    
    def stream (self, object):
        streamer = tweepy.stream(self.auth, self.listner)
        self.DataBase.save(streamer.filter(track = str(object) if type(object) != list else object))


sample = Twitter('c16icxmBoqqhpZAMFZxlWNxYo', 'cW4Y6PbYfDVe15b6yeTQjWC9Og0kTOgpQt3caIEeLreasIRNeE', '967018015849148417-21nDpxdrdkAubl7NxFOZguy8Wr7o0Dd', 'bfvCreJfsFb8ZjSjPViEGS9KSW13gWlYt4tRZYhg9OMij')
sample.search('bitcoin', 'search')
print(sample.DataBase.read())