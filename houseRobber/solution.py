from typing import List

"""
nums[k] - money in the house
P(0)=nums[0]
P(1)=max(nums[0], nums[1]) 
P(k)=max(P(k-2)+nums[k], P(k-1))
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0]*len(nums)
        result = 0
        for i in range(len(nums)):
            if i == 0:
                memo[0] = nums[0]
                result =  memo[0]
            elif i == 1:
                memo[1] = max(nums[0], nums[1])
                result = max(memo[1], memo[0])
            else:
                memo[i] = max(memo[i-2]+nums[i], memo[i-1])
                result = max(result, memo[i])
        return result
