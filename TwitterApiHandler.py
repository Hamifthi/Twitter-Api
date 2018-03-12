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

    def rateLimitStatus(self):
        return self.api.rate_limit_status()
        DataBase

    def serachTimeLine(self, id, count):
        if count > 200:
            raise ValueError('max count is 200')
        data = self.api.user_timeline(id, count = count)
        userTimeLine = DataBase.TimeLine(data = **data, name = id)
        userTimeLine.save()

    def searchTweets (self, object, lang, result_type = 'mixed', count = 200):
        if count > 200:
            raise ValueError('max count is 200')
        self.api.search(str(object) if type(object) != list else object, lang = lang, result_type = result_type)
        DataBase
    
    def stream (self, object):
        streamer = tweepy.Stream(self.auth, self.listner)
        streamer.filter(track = str(object) if type(object) != list else object)
        streamObject = DataBase.StreamObjects(data = dataDict, subject = object)
        streamObject.save()

    def cursor (self, method, **kwargs):
        items = tweepy.Cursor(method, kwargs).items()
        pages = tweepy.Cursor(method, kwargs).pages()
        return items, pages

    def api (self, method, **kwargs):
        return self.api.method(**kwargs)
        DataBase
