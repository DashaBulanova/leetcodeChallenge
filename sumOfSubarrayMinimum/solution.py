from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            result += self.find_min(arr, i)
        return result
#0(n^2)
    def find_min(self, arr: List[int], start: int) -> int:
        s, e = start, start + 1
        m = 0
        while e <= len(arr):
            m += min(arr[s:e])
            e += 1
        return m

