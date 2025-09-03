import random

class RandomizedSet:

    def __init__(self):
        self.rmap = {}
        self.rlist = []

    def insert(self, val: int) -> bool:
        if val in self.rmap:
            return False
        self.rlist.append(val)
        self.rmap[val] = len(self.rlist) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.rmap:
            return False
        self.rmap[self.rlist[-1]] = self.rmap[val]
        self.rlist[self.rmap[val]] = self.rlist[-1]
        self.rlist.pop()
        del self.rmap[val]
        return True


    def getRandom(self) -> int:
        return random.choice(self.rlist)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()