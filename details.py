import os
class detailmgr:
    fo = None
    filename=None
    details=[]
    def __init__(self,filepath=None):
        if filepath == None:
            self.filename = 'F:\\pythproj\\myFirstSpider\\detals.txt'
        else:
            self.filename = filepath
        if os.path.exists(self.filename):
            self.fo = open(self.filename, "r")
            self.details = self.fo.readlines()
            self.fo.close()

    def adddetails(self,detailpageurl):
        self.fo = open(self.filename, "a+")
        detail = detailpageurl + '\n'
        self.fo.write(detail)
        self.fo.close()

    def isDownloaded(self,url):
        if url + '\n' in self.details:
            return True
        return False

