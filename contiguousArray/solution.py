from typing import List


class Solution(object):
    #brute force approach
    def findMaxLength(self, nums: List[int]) -> int:

        max_size = 0

        for i in range(0, len(nums)):
            sum = -1 if nums[i] == 0 else 1

            for j in range(i + 1, len(nums)):
                add = -1 if nums[j] == 0 else 1
                sum += add

                if sum == 0:
                    max_size = max(max_size, j - i + 1)

        return max_size
