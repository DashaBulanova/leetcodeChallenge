from typing import List


class Solution(object):

    def moveZeroes(self, nums: List[int]) -> None:
        zero_index = -1

        for i in range(0, len(nums)):
            if nums[i] != 0:
                if zero_index != -1:
                    nums[zero_index] = nums[i]
                    nums[i] = 0
                    zero_index = min(i, zero_index+1)
            else:
                if zero_index == -1:
                    zero_index = i
