from typing import List

"""
nums[k] - money in the house
P(0)=nums[0]
P(1)=max(nums[0], nums[1]) 
P(k)=max(P(k-2)+nums[k], P(k-1))
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        result = 0
        prev, prev_prev = 0, 0
        for i in range(len(nums)):
            cur = max(prev_prev + nums[i], prev)
            result = max(result, cur)
            prev_prev = prev
            prev = result

        return result
