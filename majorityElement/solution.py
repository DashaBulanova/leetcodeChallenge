from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        required = len(nums)/2
        compress = dict()
        for n in nums:
            if n not in compress:
                compress[n] = 0
            compress[n] += 1
            if compress[n] > required:
                return n
