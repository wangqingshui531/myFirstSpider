import time

class log:
    fo = None
    filename=None

    def __init__(self,filepath=None):
        if filepath == None:
            self.filename = 'F:\pythproj\myFirstSpider\\run.info.txt'
            print('inint' + self.filename)
        else:
            self.filename = filepath

    def logruninfo(self,info):
        self.fo = open(self.filename, "a+")
        strcurtime = time.strftime("%D %H%M%S", time.localtime())
        message = str(strcurtime) + " " + info + "\n"
        self.fo.write(message)
        self.fo.close()