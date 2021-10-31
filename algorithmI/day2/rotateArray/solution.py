from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from_index = len(nums) - k
        additional = [0] * k
        j = 0

        for i in range(from_index, len(nums)):
            additional[j] = nums[i]
            j += 1

        for i in range(from_index - 1, -1, -1):
            nums[i + k] = nums[i]

        for i in range(len(additional)):
            nums[i] = additional[i]
