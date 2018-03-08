import DataBase
import tweepy
import json
dataBase = DataBase.DataBase()

class Listner(tweepy.StreamListener):

        def on_data(self, data):
            try:
                dataDict = json.loads(data)
                dataBase.save(dataDict['text'])
                dataBase.save('\n')
            except BaseException as error:
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
        self.listner = Listner()

    def search (self, object):
        dataBase.save(self.api.search(str(object) if type(object) != list else object, lang = 'en'))
    
    def stream (self, object):
        streamer = tweepy.Stream(self.auth, self.listner)
        streamer.filter(track = str(object) if type(object) != list else object)