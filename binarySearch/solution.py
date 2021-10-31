from typing import List

# [-1, 0, 3, 5, 9, 12] 9
"""
6/2=3
num[3]=5
6-3/2=1+3=4

[-1, 0, 3, 5, 9, 12] -1
index=3
index=1
index=0

[-1, 0, 3, 5, 9, 12] 2
start=0 end=5
5-0/2=2+0=2
end=2
index=0+(2/2)=1
start=1
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            index = start + int((end - start) / 2)
            if nums[index] == target:
                return index
            elif nums[index] > target:
                end = index - 1
            else:
                start = index + 1
        return -1
