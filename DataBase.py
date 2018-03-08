import pickle
class DataBase:
    def __init__ (self):
        self.database = open('Database.pickle', 'rb')

    def save (self, object):
        with open('Database.pickle', 'wb') as self.database:
            pickle.dump(object, self.database)
            pickle.dump('\n', self.database)

    def read (self):
        with open('Database.pickle', 'rb') as self.database:
            return pickle.load(self.database)
