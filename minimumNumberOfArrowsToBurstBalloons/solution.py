import math


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        result = 0

        m = -math.inf
        for i in range(len(points)):
            if points[i][0] > m:
                result += 1
                m = points[i][1]
            else:
                m = min(points[i][1], m)
        return result


"""
[[-3, -1], [1, 6], [2, 8], [7, 12], [10, 16]]
i=0
points[0][1] > m:
    result =1 
    m=-1
"""
