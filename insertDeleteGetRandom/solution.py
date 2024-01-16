import random

class RandomizedSet:
    

    def __init__(self):
        self.items_set = set()
        self.items_list = []

    def insert(self, val: int) -> bool:
        if val in self.items_set:
            result = False
        else:
            result = True
            self.items_set.add(val)
            self.items_list.append(val)
        return result

    def remove(self, val: int) -> bool:
        result = False
        if val in self.items_set:
            result = True
            self.items_set.remove(val)
            self.items_list.remove(val)
        return result
        

    def getRandom(self) -> int:
        return self.items_list[random.randint(0,len(self.items_list)-1)]

