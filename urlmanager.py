class URLManager:
    def __init__(self):
        self.urlPendings = set([])
        self.urlCrawleds = set([])

    def nextURL(self):
        if not self.urlPendings:
            return ''
        nextURL = self.urlPendings.pop()
        self.urlCrawleds.add(nextURL)
        return nextURL
    def addURL(self, url):
        if url not in self.urlCrawleds:
            self.urlPendings.add(url)
