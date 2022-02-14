from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        def searchRange(s,e)-> List[int]:
            if s==e:
                return [s,s] if nums[s] == target else [-1,-1]

            mid = s + (e-s)//2
            mid_item = nums[mid]

            if mid_item > target:
                return searchRange(s, mid)
            elif mid_item < target:
                return searchRange(mid+1, e)
            else:
                left=searchRange(s, mid)
                right=searchRange(mid+1, e)

                if left == [-1,-1]:
                    return right
                if right == [-1, -1]:
                    return left

                return [left[0], right[1]]

        return searchRange(0, len(nums)-1)


