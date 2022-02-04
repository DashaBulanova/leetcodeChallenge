from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = {0:-1}
        acc = 0
        result = 0
        for i in range(len(nums)):
            acc += 1 if nums[i] == 0 else -1
            if acc in sums:
                result = max(result, i - sums[acc])
            else:
                sums[acc]=i

        return result
