


class Solution:
    def __init__(self):
        self.global_i = 33
        self.__order = {}

    def customSortString(self, order: str, sample: str) -> str:
        i = 1
        for c in order:
            self.__order[c] = i
            i = i + 1

        return "".join(x for x in sorted(list(sample), key=self.compare))

    global_i = 33
    def compare(self, c):
        if self.__order.__contains__(c):
            return self.__order[c]
        else:
            self.global_i = self.global_i + 1
            return self.global_i
