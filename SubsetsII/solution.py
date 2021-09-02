from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(len(nums)):
            sub_result = [[nums[i]]]
            for j in range(i+1, len(nums)):
                value = sub_result[j - 1].copy()
                value.append((nums[j]))
                sub_result.append(value)
            result.append(sub_result)
        return result
