from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_index = 0
        check_index = 0

        while check_index < len(nums):
            if nums[check_index] != val:
                if check_index != insert_index:
                    nums[insert_index] = nums[check_index]
                insert_index += 1
            check_index += 1

        return insert_index
