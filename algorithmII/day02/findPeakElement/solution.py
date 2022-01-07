from typing import List

class Solution:
    def findPeak(self, nums: List[int], start: int, end: int)->int:
        if start==end:
            return start

        mid = start + (end-start)//2
        if mid > 0 and nums[mid-1]>=nums[mid]:
            return self.findPeak(nums, start, mid-1)
        if nums[mid+1]>=nums[mid]:
            return self.findPeak(nums, mid+1, end)

        return mid

    def findPeakElement(self, nums: List[int]) -> int:
        return self.findPeak(nums, 0, len(nums)-1)