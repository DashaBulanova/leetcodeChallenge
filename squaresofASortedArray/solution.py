class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []
        for i in nums:
            res.append(i*i)
        res.sort() #O(n log n)
        return res
