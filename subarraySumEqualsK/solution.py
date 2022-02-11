from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = {}
        prefixsum[0] = 1

        acc = 0
        result = 0
        for i in range(len(nums)):
            acc += nums[i]
            if acc - k in prefixsum:
                result += prefixsum[acc - k]
            prefixsum[acc] = prefixsum.get(acc, 0) + 1

        return result
