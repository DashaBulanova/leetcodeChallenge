from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        acc = 0
        for n in nums:
            acc ^= n
        return acc