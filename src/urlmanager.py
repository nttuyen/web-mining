class URLManager:
    def __init__(self, storage):
        self.urlPendings = set([])
        self.storage = storage

    def nextURL(self):
        if not self.urlPendings:
            self.urlPendings = self.storage.getURLs(0, 1000)
        if not self.urlPendings:
            return ''
        nextURL = self.urlPendings.pop()
        #self.storage.crawledURL(nextURL)
        return nextURL
    
    def addURL(self, url, ref = ''):
        self.storage.addURL(url, ref)
