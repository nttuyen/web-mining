class VGHMTLProcessor:
    def __init__(self, storage):
        self.storage = storage
        
    def process(self, url, content):
        print('store content ', url, ' content=', content)
        self.storage.saveContentOfURL(url, content);
        