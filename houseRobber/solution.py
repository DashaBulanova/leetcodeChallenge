from typing import List

"""
nums[k] - money in the house
P(0)=nums[0]
P(1)=max(nums[0], nums[1]) 
P(k)=max(P(k-2)+nums[k], P(k-1))
"""
class Solution:
    __memo = {}

    def __init__(self):
        self.__memo = {}

    def rob(self, nums: List[int]) -> int:
        return self.__calculate_max(len(nums) - 1, nums)

    def __calculate_max(self, k, nums):
        if k == 0:
            self.__memo[0] = nums[0]
            return nums[0]
        if k == 1:
            self.__memo[1] = max(nums[0], nums[1])
            return self.__memo[1]

        if k - 2 in self.__memo:
            k_2 = self.__memo[k - 2]
        else:
            k_2 = self.__calculate_max(k - 2, nums)
            self.__memo[k - 2] = k_2

        if k - 1 in self.__memo:
            k_1 = self.__memo[k - 1]
        else:
            k_1 = self.__calculate_max(k - 1, nums)
            self.__memo[k - 1] = k_1

        return max([k_2 + nums[k], k_1])
