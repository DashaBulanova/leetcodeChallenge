from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, arr: List[int], target: int) -> int:
        if target == 0:
            return 0
        
        start = 0
        acc = 1
        result = 0
        for end in range(len(arr)):
            acc *= arr[end]
            while acc >= target and start<=end:
                acc /= arr[start]
                start += 1
            result += end-start+1
        return result
