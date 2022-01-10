from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, arr: List[int], target: int) -> int:
        start = 0
        acc = 1
        result = 0
        for end in range(len(arr)):
            acc *= arr[end]
            while start<=end and acc >= target:
                acc /= arr[start]
                start += 1
            result += end+1-start

        return result
