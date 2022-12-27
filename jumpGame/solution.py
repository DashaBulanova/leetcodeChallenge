class Solution:
    def __init__(self) -> None:
        self. __memo = {}

    def canJump(self, nums: list[int]) -> bool:
        return self.__can_jump(0, nums)

    def __can_jump(self, s, nums: list[int]) -> bool:
        if s > len(nums) - 1:
            return False
        if s == len(nums) - 1:
            return True
        m = nums[s]
        if m == 0:
            return False
        start = len(nums)-1 if s+m >= len(nums)-1 else s+m
        for j in range(start, s, -1):
            if j in self.__memo:
                continue
            if self.__can_jump(j, nums):
                return True
            else:
                self.__memo[j] = False
        return False
