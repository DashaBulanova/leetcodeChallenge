from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        return self.findNonDuplicate(0, len(nums) - 1, nums)

    def findNonDuplicate(self, left, right, nums) -> int:
        if left == right:
            return nums[left]

        mid = left + (right - left) // 2

        if mid % 2 == 0:
            if nums[mid + 1] == nums[mid]:
                return self.findNonDuplicate(mid + 2, right, nums)
            else:
                return self.findNonDuplicate(left, mid - 2, nums)
        else:
            if nums[mid - 1] == nums[mid]:
                return self.findNonDuplicate(mid + 1, right, nums)
            else:
                return self.findNonDuplicate(left, mid - 1, nums)
