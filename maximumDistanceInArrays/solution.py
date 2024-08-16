import math


class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        res = 0
        min_, max_ = math.inf, -math.inf
        for i in range(len(arrays)):
            res = max(res, arrays[i][-1] - min_, max_ - arrays[i][0])
            min_ = min(min_, arrays[i][0])
            max_ = max(max_, arrays[i][-1])
        return res
