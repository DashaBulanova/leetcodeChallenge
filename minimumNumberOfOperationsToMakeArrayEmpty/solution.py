import math


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        result = 0
        for k,v in d.items():
           if v == 1:
               return -1
           result += math.ceil(v/3)
        return result
