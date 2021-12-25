from typing import List

class Solution:

    def search(self, nums: List[int], target: int, start: int, end: int)-> List[int]:
        if start == end:
            return [start,start] if nums[start] == target else [-1,-1]

        mid = start + int((end-start)/2)
        mid_item = nums[mid]

        if mid_item < target:
            return self.search(nums, target, mid+1, end)
        
        if mid_item > target:
            return self.search(nums, target, start, mid-1)

        left = self.search(nums, target, start, mid-1)
        right = self.search(nums, target, mid+1, end)

        return [mid if left[0]==-1 else left[0], max(right[1], mid)]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]

        return self.search(nums, target, 0, len(nums)-1)