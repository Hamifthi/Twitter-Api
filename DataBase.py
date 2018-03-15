import datetime
from mongoengine import *

def __init__ (dataBaseName):
    connect(dataBaseName)

class rateLimitStatus(Document):
    data = DictField(required = True)
    time = DateTimeField(default =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class TimeLine(Document):
    data = DictField()
    name = StringField(required = True)
    time = DateTimeField(default =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class Tweets(Document):
    data = DictField()
    subject = StringField(required = True)
    time = DateTimeField(default =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class StreamObjects(Document):
    data = DictField()
    subject = StringField(default = None)
    time = DateTimeField(default =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class CursorObjects(Document):
    items = DictField()
    pages = DictField()
    method = StringField(default = None)
    time = DateTimeField(default =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class ApiObjects(Document):
    data = DictField()
    method = StringField(default = None)
    time = DateTimeField(default =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))