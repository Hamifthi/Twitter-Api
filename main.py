import DataBase
import TwitterApiHandler

sample = TwitterApiHandler.Twitter('c16icxmBoqqhpZAMFZxlWNxYo', 'cW4Y6PbYfDVe15b6yeTQjWC9Og0kTOgpQt3caIEeLreasIRNeE', '967018015849148417-21nDpxdrdkAubl7NxFOZguy8Wr7o0Dd', 'bfvCreJfsFb8ZjSjPViEGS9KSW13gWlYt4tRZYhg9OMij')
#sample.search(['bitcoin', 'etherum'])
#sample.stream(['bitcoin'])
sample.stream('bitcoin')