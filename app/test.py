__author__ = 'zhenghong'

class Kls(object):
    def __init__(self, data):
        self.data = data

    @classmethod
    def printd(self):
        print(self.data)

ik1 = Kls('arun')
ik2 = Kls('seema')
ik2.printd()


