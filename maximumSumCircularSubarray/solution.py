from math import floor
from typing import List


class Solution(object):
    # idea:
    # corner cases:
    #   1. all items in array is positive - then maximum is sum of all items
    #   2. all items is negative then maximum is minimum item of array
    # for general case:
    # 1. use Kadane's algorithm to find non-circular max subarray
    # 2. use Kadane's algorithm to find circular min subarray
    # 3. find total sum of array and
    def maxSubArray(self, nums: List[int]) -> int:
        total_sum, current_sum_min, current_sum_max = 0, 0, 0
        min_sum, max_sum = nums[0], nums[0]

        for i in nums:
            current_sum_min = min(i, current_sum_min + i)
            current_sum_max = max(i, current_sum_max + i)

            max_sum = max(max_sum, current_sum_max)
            min_sum = min(min_sum, current_sum_min)

            total_sum += i

        if total_sum == min_sum:
            return max_sum

        return max(max_sum, (total_sum - min_sum))
