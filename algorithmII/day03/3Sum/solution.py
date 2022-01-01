from typing import List


class Solution:
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        result = []
        end = len(nums) - 1
        while start < end:
            if nums[start] + nums[end] == target:
                result.append([-target, nums[start], nums[end]])
                s_p = nums[start]
                while nums[start] == s_p and start < end:
                    start += 1
                e_p = nums[end]
                while nums[end] == e_p and end > start:
                    end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1

        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        result = []
        prev = None
        for i in range(0, len(nums)):  # time comp O(log n)+O(n)
            if prev is None or nums[i] != prev:
                result.extend(self.twoSum(nums, i + 1, target=-nums[i]))
                prev = nums[i]
        return result
