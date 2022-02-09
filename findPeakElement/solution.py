from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def findPeak(s, e) -> int:
            mid = s + (e - s) // 2
            mid_item = nums[mid]

            if mid != 0 and mid_item < nums[mid-1]:
                return findPeak(s, mid)
            if mid < len(nums) - 1 and mid_item < nums[mid+1]:
                return findPeak(mid + 1, e)
            else:
                return mid

        return findPeak(0, len(nums) - 1)
