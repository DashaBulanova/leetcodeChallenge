from typing import List


class MedianFinder:

    def __init__(self):
        self.df = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.df.append(num)
        self.df = sorted(self.df)

    def findMedian(self) -> float:
        if len(self.df) % 2 > 0:
            index = int((len(self.df) - 1) / 2)
            return float(self.df[index])
        # size of list is odd
        else:
            index = int((len(self.df) - 1) // 2)
            return (self.df[index] + self.df[index+1])/2
