from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        forward, backward = [0] * len(nums), [0] * len(nums)

        forward[0] = 1
        for i in range(1, len(nums)):
            forward[i] = forward[i - 1] * nums[i - 1]

        backward[len(nums)-1] = 1
        for j in range(len(nums)-2, -1, -1):
            backward[j] = backward[j+1] * nums[j+1]

        result = [0] * len(nums)
        for i in range(0, len(nums)):
            result[i] = forward[i] * backward[i]

        return result
