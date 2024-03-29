import re
from time import sleep
import urllib2
import urlparse

class URLRequest:
    def __init__(self, fileName):
        self.noOfURL = 0
        self.file = open(fileName, 'a')
        self.linkPattern = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')
    def __del__(self):
        self.file.close()

    def execute(self, requestURL, urlManager, processor):
        self.noOfURL = self.noOfURL + 1
        print '{0:9d}: {1}'.format(self.noOfURL, requestURL)
        self.file.write('{0:9d}: {1}'.format(self.noOfURL, requestURL))
        self.file.write("\n")
        self.file.flush()

        url = urlparse.urlparse(requestURL)
        try:
            response = urllib2.urlopen(requestURL, None, 120)
            content = response.read()
            links = self.linkPattern.findall(content)
            for link in (links.pop(0) for _ in xrange(len(links))):
                if link.startswith('/'):
                    link = 'http://' + url[1] + link
                elif link.startswith('#'):
                    link = 'http://' + url[1] + url[2] + link
                elif not link.startswith('http'):
                    link = 'http://' + url[1] + '/' + link

                if link.find(url[1]) == -1:
                    continue
                urlManager.addURL(link, requestURL)
            #process content
            if content.find('<html>') == -1:
                print('access denine content')
                sleep(3600)
            else:
                processor.process(requestURL, content)
        except:
            print 'Exception on load url'
            return
        
        
        
