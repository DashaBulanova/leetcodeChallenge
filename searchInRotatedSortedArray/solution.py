from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        s,e=0, len(nums)-1
        while s<e:
            mid=s+(e-s)//2
            if nums[mid]==target:
                return mid

            if nums[s]<=nums[mid]:
                if nums[s]<=target<nums[mid]:
                    e=mid
                else:
                    s=mid+1
            else:
                if nums[mid]<target<=nums[e]:
                    s=mid+1
                else:
                    e=mid

        return s if nums[s] == target else -1