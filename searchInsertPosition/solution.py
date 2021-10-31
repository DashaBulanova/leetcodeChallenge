from typing import List

#[1, 3, 5, 6], 0
"""
start =0
end = 3

index = 0 + 1 = 1
end = 0

index=0

"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            index = start + int((end - start) / 2)
            if nums[index] == target:
                return index
            elif nums[index] > target:
                end = index - 1
            else:
                start = index + 1

        return start

