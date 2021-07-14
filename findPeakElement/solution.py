from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.findPeak(nums, 0, len(nums)-1)

    def findPeak(self, nums: List[int], start: int, end: int):
        mid = start + int((end - start)/2)
        if (mid + 1 <= len(nums) - 1) and nums[mid] < nums[mid + 1]:
            return self.findPeak(nums, mid + 1, end)
        elif mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
            return self.findPeak(nums, start, mid - 1)
        else:
            return nums[mid]
