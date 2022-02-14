from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        s,e=0,len(nums)-1
        while s<=e:
            mid=s+(e-s)//2
            if mid<len(nums)-1 and nums[mid]<nums[mid+1]:
                s=mid+1
            elif mid>0 and nums[mid-1]>nums[mid]:
                e=mid
            else:
                return mid
