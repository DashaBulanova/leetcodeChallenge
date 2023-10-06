from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        first_run = True

        def next(index):
            return nums[index]

        while first_run or slow != fast: 
            first_run = False
            slow = next(slow)
            fast = next(next(fast))

        slow = 0
        while slow != fast:
            slow = next(slow)
            fast = next(fast)
        return fast
