from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = set()
        times = len(nums) / 3
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
            if map[nums[i]] > times:
                result.add(nums[i])
        return list(result)
