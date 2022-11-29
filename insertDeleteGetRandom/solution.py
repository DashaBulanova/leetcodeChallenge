from random import randrange


class RandomizedSet:

    def __init__(self):
        self.k = set()

    def insert(self, val: int) -> bool:
        if val in self.k:
            return False
        self.k.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.k:
            self.k.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        r = randrange(len(self.k))
        return list(self.k)[r]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
