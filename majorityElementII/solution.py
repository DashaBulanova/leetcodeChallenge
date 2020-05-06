from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        required = int(len(nums)/3)
        nums = sorted(nums)
        result = set()
        prev = None
        count = 0
        for n in nums:
            if prev is None or prev != n:
                prev = n
                count = 0
            if prev == n:
                count += 1
                if count > required:
                    result.add(n)

        return list(result)