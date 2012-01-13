import sqlite3
class SQLiteDBStorage:
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = sqlite3.connect(dbname)
        self.connection.isolation_level = None

    def __del__(self):
        self.connection.close()
    
    def addURL(self, url, ref):
        try:
            query = "insert into url_queue(url, refer, crawled) values ('{0}', '{1}', {2})".format(url, ref, 0)
            cur = self.connection.cursor()
            cur.execute(query)
            self.connection.commit()
            cur.close()
            return 1
        except:
            return 0

    def crawledURL(self, url):
        try:
            query = "update url_queue set crawled = 1 where url = ?"
            cur = self.connection.cursor()
            cur.execute(query, (url))
            self.connection.commit()
            cur.close()
        except:
            return 0

    def getURLs(self, state, limit):
        try:
            query = 'select url from url_queue where crawled = ? order by url limit ?'
            cur = self.connection.cursor()
            cur.execute(query, (state, limit))
            result = cur.fetchall()
            cur.close()
            
            _return = set([])
            for r in result:
                _return.add(r[0])

            return _return
        except:
            return set([])


import MySQLdb
class MySQLDBStorage:
    def __init__(self, host, username, password, dbname):
        self.dbname = dbname
        self.connection = MySQLdb.connect(host, username, password, dbname)

    def __del__(self):
        self.connection.close()

    def addURL(self, url, ref):
        try:
            query = "insert into url_queue(url, refer, crawled) values ('{0}', '{1}', {2})".format(url, ref, 0)
            cur = self.connection.cursor()
            cur.execute(query)
            self.connection.commit()
            cur.close()
            return 1
        except:
            return 0

    def crawledURL(self, url):
        try:
            query = "update url_queue set crawled = 1 where url = %s"
            cur = self.connection.cursor()
            cur.execute(query, (url))
            self.connection.commit()
            cur.close()
        except:
            return 0

    def getURLs(self, state, limit):
        try:
            query = 'select url from url_queue where crawled = %s order by url limit %s'
            cur = self.connection.cursor()
            cur.execute(query, (state, limit))
            result = cur.fetchall()
            cur.close()

            _return = set([])
            for r in result:
                _return.add(r[0])

            return _return
        except:
            return set([])

    def saveContentOfURL(self, url, content):
        try:
            query = "update url_queue set crawled = 1, data=%s where url = %s"
            cur = self.connection.cursor()
            cur.execute(query, (content, url))
            self.connection.commit()
            cur.close()
            return 1
        except:
            return 0
