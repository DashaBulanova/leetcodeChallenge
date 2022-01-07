
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while start < end:
            mid = start + (end - start)//2

            if nums[start]<=nums[mid]<nums[end]: # линия
                return nums[start]
            
            if nums[mid]>nums[end]:
                start = mid+1
            else:# nums[mid]<nums[end] and nums[start]>nums[mid]:
                end = mid

        return nums[start]