class DataBase:
    def __init__ (self):
        self.database = open('Database.json', 'a', encoding = 'utf8')

    def save (self, object):
        self.database.write(object)
        self.database.write('\n')
        self.database.close()

    def read (self, object):
        with open('Database.json', 'r') as database:
            return database.read(object)
