from typing import List


class Solution:
    #divide and conque approach O(log(n))
    def findPeakElement(self, nums: List[int]) -> int:
        return self.find_peak(nums, 0, len(nums))

    def find_peak(self, nums: List[int], start, end) -> int:
        mid = start + int((end - start) / 2)
        if nums[mid] < nums[mid - 1]:
            return self.find_peak(nums, start, mid - 1)
        elif len(nums) > mid+1 and nums[mid] < nums[mid+1]:
            return self.find_peak(nums, mid+1, end)
        else:
            return mid
