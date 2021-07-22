from itertools import combinations
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        result = 0
        #кол-во сочетаний без повторений
        for pair in combinations(nums, 3): #O(n! / (n-k)!k!)
            #Triangle Inequality Theorem
            if pair[0] + pair[1] > pair[2] and pair[1] + pair[2] > pair[0] and pair[0] + pair[2] > pair[1]:
                result += 1

        return result
