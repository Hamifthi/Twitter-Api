import DataBase
import tweepy
import json
import datetime
from textblob import TextBlob

class Listner(tweepy.StreamListener):

    def on_data(self, data):

        # try:
        #     data = json.loads(data, encoding = 'UTF_8')
        #     DataBase.connect('TweetDB')
        #     streams = DataBase.StreamObjects()
        #     streams.data.new_file(encoding = 'UTF_8', type = 'string')
        #     streams.data.write("hi")
        #     streams.data.close()

        try:
            data = json.loads(data, encoding = 'UTF_8')
            dataBase = open('tweetDB.txt', 'a', encoding = 'utf8')
            # dataBase.write(str([data[key] for key in ['retweet_count', 'created_at', 'text', 'entities']]))
            dataBase.write(str(data['text']))
            dataBase.write('\n')
            dataBase.close()
        except BaseException as error:
            print(error)

    def on_error(self, status):
        print(status)

class Twitter:
    
    def __init__ (self, consumerKey, consumerSecret, accessToken, accessSecret, dataBaseName):
        self.consumerKey = consumerKey
        self.consumerSecret = consumerSecret
        self.accessToken = accessToken
        self.accessSecret = accessSecret
        self.auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        self.auth.set_access_token(self.accessToken, self.accessSecret)
        self.api = tweepy.API(self.auth, parser = tweepy.parsers.JSONParser())
        self.listner = Listner()
        DataBase.connect(dataBaseName)

    def rateLimitStatus(self):
        DataBase.rateLimitStatus(data = {'status' : self.api.rate_limit_status()}).save()
        return self.api.rate_limit_status()

    def searchTimeLine(self, id, count):
        if count > 200:
            raise ValueError('max count is 200')
        DataBase.TimeLine({'data' : self.api.user_timeline(id, count = count)}, name = str(id)).save()
        return self.api.user_timeline(id, count = count)

    def searchTweets (self, object, lang, count = 200):
        if count > 200:
            raise ValueError('max count is 200')
        DataBase.Tweets({'data' : self.api.search(object, lang = lang)}, subject = str(object)).save()
        return self.api.search(object, lang = lang)
    
    def stream (self, object):
        streamer = tweepy.Stream(self.auth, self.listner)
        streamer.filter(track = [object], languages = ["en"])