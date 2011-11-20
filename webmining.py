

if __name__ == "__main__":
    import sys
    rootURL = ''
    if len(sys.argv) > 1:
        rootURL = sys.argv[1]
    else:
        rootURL = 'vatgia.com'
    print 'Crawl ', rootURL

    from urlmanager import URLManager
    from urlrequest import URLRequest
    urlManager = URLManager()
    urlManager.addURL('http://{0}'.format(rootURL))
    urlManager.addURL('http://{0}/home'.format(rootURL))
    urlManager.addURL('http://{0}/home/'.format(rootURL))

    urlRequest = URLRequest('testlink.txt')
    while 1:
        nextURL = urlManager.nextURL()
        if not nextURL:
            break
        urlRequest.execute(nextURL, urlManager)
    
