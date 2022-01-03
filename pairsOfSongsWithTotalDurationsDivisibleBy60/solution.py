import math
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result = 0
        dic = {}
        for i in time:  # time comp O(n)
            key = i if i < 60 else i % 60
            val = dic[key] + 1 if key in dic else 1
            dic[key] = val

        for key, val in dic.items():
            if val == 0:
                continue
            if key == 0 or key == 30:
                if val != 1:
                    result += int(math.factorial(val) / (math.factorial(val - 2) * 2))
            else:
                target = 60 - key
                if target in dic and dic[target] != 0:
                    result += dic[target] * val
                    dic[target] = 0
                    dic[key] = 0

        return result
