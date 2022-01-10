import math
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        result = math.inf
        acc = 0
        for end in range(len(nums)):
            acc += nums[end]
            while acc >= target:
                result = min(result, end-start+1)
                acc -= nums[start]
                start += 1

        return 0 if result==math.inf else result
