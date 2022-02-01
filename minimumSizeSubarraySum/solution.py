from typing import List
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        acc = 0
        result = math.inf
        for end in range(len(nums)):
            acc += nums[end]
            while acc>=target:
                result = min(result, end-start+1)
                acc -= nums[start]
                start += 1

        return result if result != math.inf else 0