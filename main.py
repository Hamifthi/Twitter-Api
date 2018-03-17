import DataBase
import TwitterApiHandler
import datetime
import time
DataBase.connect('TweetDB')

sample = TwitterApiHandler.Twitter('c16icxmBoqqhpZAMFZxlWNxYo', 'cW4Y6PbYfDVe15b6yeTQjWC9Og0kTOgpQt3caIEeLreasIRNeE', '967018015849148417-21nDpxdrdkAubl7NxFOZguy8Wr7o0Dd', 'bfvCreJfsFb8ZjSjPViEGS9KSW13gWlYt4tRZYhg9OMij', 'TweetDB')
#sample.stream(['bitcoin', 'etheruem'])
# items = sample.cursor(sample.api.friends, user_id = 'alireza29675')[0]
# sample.searchTweets('bitcoin', lang = 'en')
sample.stream('Bitcoin')