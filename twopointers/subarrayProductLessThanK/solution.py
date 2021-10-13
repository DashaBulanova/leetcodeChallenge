from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, arr: List[int], target: int) -> int:
        start = 0
        acc = 1
        result = 0

        for end in range(len(arr)):
            if arr[end] < target:
                acc *= arr[end]
                while acc >= target:
                    acc /= arr[start]
                    start += 1

                result += end - start + 1
            else:
                start = end + 1
                acc = 1

        return result
