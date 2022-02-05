import math
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # O(n log n)
        result = []

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = [i]

        def twoSum(start: int, target) -> List[List[int]]:
            res = []
            prev = None
            for i in range(start + 1, len(nums)):
                if prev is not None and nums[i] == prev:
                    continue

                if target - nums[i] in hashmap:
                    for j in hashmap[target - nums[i]]:
                        if i < j:
                            res.append([nums[start], nums[i], nums[j]])
                            break
                prev = nums[i]

            return res

        prev = None
        for i in range(len(nums)):  # 0(n)
            if prev is not None and nums[i] == prev:
                continue
            else:
                res = twoSum(i, -nums[i])
                result.extend(res)
            prev = nums[i]

        return result
