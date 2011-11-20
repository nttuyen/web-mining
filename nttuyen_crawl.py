import sys
import re
import urllib2
import urlparse

rooturl = 'vatgia.com';
tocrawl = set(['http://{0}'.format(rooturl), 'http://{0}/home'.format(rooturl), 'http://{0}/home/'.format(rooturl)])
crawled = set(['http://{0}'.format(rooturl), 'http://{0}/home'.format(rooturl), 'http://{0}/home/'.format(rooturl)])
linkregex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')

noOfLink = 0
f = open('links_vg.txt', 'w')

while 1:
    try:
        crawling = tocrawl.pop()
        noOfLink = noOfLink + 1
        print '{0:9d}: {1}'.format(noOfLink, crawling)
        f.write('{0:9d}: {1}'.format(noOfLink, crawling))
        f.write("\n")
        f.flush()
    except KeyError:
        f.close()
        raise StopIteration
    url = urlparse.urlparse(crawling)
    try:
        response = urllib2.urlopen(crawling)
    except:
        print 'Exception on load url'
        continue
    msg = response.read()
    links = linkregex.findall(msg)
    crawled.add(crawling)
    
    for link in (links.pop(0) for _ in xrange(len(links))):
        if link.startswith('/'):
            link = 'http://' + url[1] + link
        elif link.startswith('#'):
            link = 'http://' + url[1] + url[2] + link
        elif not link.startswith('http'):
            link = 'http://' + url[1] + '/' + link

        if link.find(rooturl) == -1:
            continue
            
        if link not in crawled:
            tocrawl.add(link)
