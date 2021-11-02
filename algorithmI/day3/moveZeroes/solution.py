from typing import List

"""
[0, 1, 0, 3, 12]

"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(index_1: int, index_2: int):
            if index_2 == index_1:
                return
            c = nums[index_1]
            nums[index_1] = nums[index_2]
            nums[index_2] = c

        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                swap(zero_index, i)
                zero_index += 1
