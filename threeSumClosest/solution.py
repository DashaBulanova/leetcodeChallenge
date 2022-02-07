import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        result = math.inf, 0
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                diff = target - nums[i] - nums[l] - nums[r]
                if diff == 0:
                    return nums[i] + nums[l] + nums[r]
                data = [result, (abs(diff), nums[i] + nums[l] + nums[r])]
                result = min(data, key=lambda t: t[0])
                if diff > 0:
                    l += 1
                else:
                    r -= 1

        return result[1]
