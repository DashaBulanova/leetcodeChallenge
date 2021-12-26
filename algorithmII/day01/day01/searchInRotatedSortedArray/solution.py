from typing import List

class Solution:
    def search_rec(self, nums: List[int], target: int, start:int, end: int) -> int:
        if start == end:
            return start if nums[start] == target else -1

        mid = start + int((end-start)/2)
        mid_item = nums[mid]

        if mid_item == target:
            return mid

        if nums[start] <= mid_item: #this part is not rotated 
            if nums[start] <= target < mid_item:
                end = mid
            else:
                start = mid +1
        else:
             if mid_item < target <=nums[end]:
                start = mid+1
             else: 
                end = mid
        return self.search_rec(nums, target, start, mid)



    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        return self.search_rec(nums, target, 0, len(nums)-1)
