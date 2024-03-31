import random


class RandomizeSet(object):

    def __init__(self):
        self.lst=[]
        self.map={}

    def search(self,val):
        return val in self.map

    def insert(self,val):
        if self.search(val):
            return False
        self.lst.append(val)
        self.map[val] = len(self.lst) -1
        return True

    def remove(self,val):
        if not self.search(val):
            return False
        idx=self.map[val]
        self.lst[idx] = self.lst[-1]
        self.map[self.lst[-1]] = idx
        self.lst.pop()
        del self.map[val]
        return True

    def getRandom(self):
        return random.choice(self.lst)