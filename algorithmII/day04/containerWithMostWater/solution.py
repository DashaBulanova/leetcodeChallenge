from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        result = 0
        count = len(height)
        while start < end:
            volume = min(height[start], height[end]) * (end-start)
            result = max(result, volume)
            if height[start] > height[end]:
                end -= 1
            elif height[start] < height[end]:
                start += 1
            else:
                end -= 1
                start +=1

        return result
