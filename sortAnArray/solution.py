from heapq import heappush, heappop

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        h = []
        for n in nums:
            heappush(h, n)

        result = [0]*len(nums)
        for i in range(len(nums)):
            result[i]=heappop(h)
        return result

