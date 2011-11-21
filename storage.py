import sqlite3
class SQLiteDB:
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)

    def __del__(self):
        self.connection.close()
    
    def addURL(self, url, ref):
        try:
            query = 'insert into url_queue(url, refer, crawled) value({0}, {1}, {2})'.format(url, ref, 0)
            cur = self.connection.cursor()
            cur.execute(query)
            self.connection.commit()
            cur.close()
            return 1
        except:
            return 0

    def getURLs(self, state, limit):
        try:
            query = 'select url from url_queue where crawled = ?'
            cur = self.connection.cursor()
            cur.execute(query, ())
        except:
            return set([])
