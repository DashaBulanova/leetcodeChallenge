from typing import List

"""
[[2,5], [7,9]], [1,10]
i=0 interval = [2,5]
5<1 False
return -1

example 2: [[2,5], [7,9]], [7,10]
i=0 interval = [2,5]
2<7 True
res=0

i=0 interval = [2,5]
"""


def find_insert_index(intervals: List[List[int]], newInterval):
    res = -1
    for i in range(len(intervals)):
        interval = intervals[i]
        if interval[0] < newInterval[0]:
            res = i
        else:
            return res
    return res


"""
1.
      [5,7]   [11,13]
[1,3]  
b[1]<a[0]
result = [[1,3] [5,7] [11,13]]
2.
[1,3]        [11,13]
      [5,7]  
a[1]<b[0]
result = [[1,3] [5,7] [11,13]]
3.
[1,3]    [7,9]
  [2,5]
a[0]<=b[0]<=a[1]<=b[1]
result = [[1,5] [7,9]]
4.
  [2,3]    [7,9]
[1,5]
b[0]<=a[0]<=b[1]<=a[1]
result = [[1,5] [7,9]]
5.
[1,3]    [7,9]   
  [2,      8]
a[0]<=b[0]<=a[1]<=b[1]
result = [[1,9]]
6.
[1,3]    [7,9] 
       [6 ,8]
result = [[1,3], [6,9]]
7
[1,3]    [7,9] 
           [8,11]
result = [[1,3], [7,11]]
8
[1,3]    [7,9] 
               [11,13]
result = [[1,3], [7,9], [11,13]]

"""


class Solution:
    def insert(self,
               intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        result = []
        i = 0
        # skip all intervals before newInterval start
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        merged_interval = newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            merged_interval[0] = min(intervals[i][0], merged_interval[0])
            merged_interval[1] = max(intervals[i][1], merged_interval[1])
            i += 1

        result.append(merged_interval)
        result.extend(intervals[i:len(intervals)])
        return result
