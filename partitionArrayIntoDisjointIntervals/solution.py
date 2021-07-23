from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max_left = nums[0]

        start = 1
        end = len(nums) - 1
        left_count = 1

        while start < len(nums) - 1:
            max_value, min_value, min_index = self.__get_min(nums, start, end)
            if min_value < max_left:
                left_count = 1 + min_index
                max_left = max(max_value, max_left)
                start = min_index + 1
            else:
                return left_count

        return left_count

    def __get_min(self, nums, start, end):
        min_value = nums[start]
        min_index = start
        for i in range(start + 1, end):
            if nums[i] < min_value:
                min_value = nums[i]
                min_index = i

        max_value = max(nums[start:min_index]) if start != min_index else min_value

        return max_value, min_value, min_index
