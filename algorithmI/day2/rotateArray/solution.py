import math
from typing import List


def right_rotate(nums):
    last_element = nums[len(nums) - 1]
    for i in range(len(nums) - 1, 0, -1):
        nums[i] = nums[i - 1]
    nums[0] = last_element


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)%k == 0:
            for i in range(k, -1, -1):
                index_from = len(nums) - i
                  #  index_to=shift_index
                item = nums[shift_index]

