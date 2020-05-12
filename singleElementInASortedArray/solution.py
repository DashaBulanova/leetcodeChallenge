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
                elif nums[mid - 1] == nums[mid]:
                    right = mid - 2
                else:
                    return nums[mid]
            else:
                if nums[mid + 1] == nums[mid]:
                    right = mid - 1
                elif nums[mid - 1] == nums[mid]:
                    left = mid + 1
                else:
                    return nums[mid]

        return nums[left]
