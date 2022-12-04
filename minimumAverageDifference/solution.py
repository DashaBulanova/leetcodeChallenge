import math
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        right_sum, left_sum = 0, sum(nums)
        n = len(nums)
        min_diff = (math.inf, None)
        for i in range(len(nums)):
            right_sum += nums[i]
            left_sum -= nums[i]
            if left_sum == 0:
                avr_diff = abs(int(right_sum / (i + 1)))
            else:
                avr_diff = abs(int(right_sum / (i + 1)) - int(left_sum / (n - (i + 1))))
            min_diff = min([min_diff, (avr_diff, i)], key=lambda t: t[0])

        return int(min_diff[1])
