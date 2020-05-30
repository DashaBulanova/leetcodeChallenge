from math import floor
from typing import List


class Solution(object):

    def maxSubArray(self, nums: List[int]) -> int:
        return self.kadane_approach(nums)

    def kadane_approach(self, nums: List[int]) -> int:
        current_sum, max_sum = 0, None

        for i in nums:
            current_sum = max(i, current_sum + i)
            if max_sum is None:
                max_sum = current_sum
            max_sum = max(max_sum, current_sum)

        return max_sum

    def divide_and_conquer_approach(self, nums: List[int]) -> int:
        return self.max_sub_array(0, len(nums) - 1, nums)

    # l - левая граница, r - правая граница
    def max_sub_array(self, le: int, r: int, nums: List[int]) -> int:

        if le == r:
            return nums[le]

        q = floor((r - le) / 2)

        left_sum = self.max_sub_array(le, le + q, nums)
        right_sum = self.max_sub_array(le + q + 1, r, nums)
        crossing_sum = self.sum_crossing(le, le + q, r, nums)

        return max(left_sum, right_sum, crossing_sum)

    # l - левая граница, r - правая граница, q - середина
    def sum_crossing(self, le: int, q: int, r: int, nums: List[int]) -> int:
        sum = 0
        l_max = 0

        for i in reversed(range(le, q + 1)):
            sum += nums[i]
            if sum > l_max or l_max == 0:
                l_max = sum

        sum = 0
        r_max = 0
        for i in range(q + 1, r + 1):
            sum += nums[i]
            if sum > r_max or r_max == 0:
                r_max = sum

        return r_max + l_max
