from random import randrange

class RandomizedSet:

    def __init__(self):
        self.k = dict()
        self.r = list()

    def insert(self, val: int) -> bool:
        if val in self.k:
            return False
        self.r.append(val)
        self.k[val] = len(self.r)-1
        return True

    def remove(self, val: int) -> bool:
        if val in self.k:
            j = self.k[val]
            self.r[j] = self.r[-1]
            self.k[self.r[j]] = j
            self.k.pop(val)
            del self.r[-1]
            return True
        return False

    def getRandom(self) -> int:
        return self.r[randrange(len(self.r))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()