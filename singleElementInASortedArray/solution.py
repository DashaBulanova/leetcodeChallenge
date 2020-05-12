from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left != right:
            mid = left + (right - left) // 2

            if mid % 2 == 0:
                if nums[mid + 1] == nums[mid]:
                    left = mid + 2
                else:
                    right = mid - 2
            else:
                if nums[mid + 1] == nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return nums[left]
