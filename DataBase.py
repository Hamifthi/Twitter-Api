import pickle
class DataBase:
    def __init__ (self):
        self.database = open('Database.pickle', 'wb')

    def save (self, objectName, object):
        pickle.dump(dict(objectName = object), self.database)
        pickle.dump('\n', self.database)
        self.database.close()

    def read (self):
        with open('Database.pickle', 'rb') as self.database:
            return pickle.load(self.database)
