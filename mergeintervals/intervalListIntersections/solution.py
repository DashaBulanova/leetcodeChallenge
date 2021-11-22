from typing import List

"""

[[3,5],[9,20]]
[[4,5],[7,10],[11,12],[14,15],[16,20]]

first = 0
second = 0

step 0: 0<2 and 0<5:
a = [3,5]
b=[4,5]
#1 intersection = [[4,5]]
second = 1

step 1: 0<2 and 1<5:
a = [3,5]
b=[7,10]
#1 intersection = [[4,5]]
first = 1

step 1: 1<2 and 1<5:
a = [9,20]
b=[7,10]
#1 intersection = [[4,5], [9, 10]]
second = 2
first = 1

step 2: 1<2 and 2<5:
a = [9,20]
b=[11,12]
#1 intersection = [[4,5], [9, 10],[11,12]]
second = 3
first = 1

step 3: 1<2 and 3<5:
a = [9,20]
b=[14,15]
#1 intersection = [[4,5], [9, 10],[11,12], [14,15]]
second = 4
first = 1

step 3: 1<2 and 4<5:
a = [9,20]
b=[16,20]
#1 intersection = [[4,5], [9, 10],[11,12], [14,15], [16,20]]
second = 5
first = 1

"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        index_a = 0
        index_b = 0

        while index_a < len(firstList) and index_b < len(secondList):
            # do not have overlapping
            a = firstList[index_a]
            b = secondList[index_b]
            # do not have overlapping
            if a[1] < b[0]:
                index_a += 1
            elif b[1] < a[0]:
                index_b += 1
            else:
                # has overlapping
                result.append([max(b[0], a[0]), min(b[1], a[1])])
                index_a += int(b[1] >= a[1])
                index_b += int(b[1] < a[1])

        return result



"""
[[0,2],[5,10],[13,23],[24,25]]
[[1,5],[8,12],[15,24],[25,26]]
[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])

[0,2], [1,5], [5,10], [8,12], [13,23], [15,24],[24,25],[25,26]

step 0: index = 1
current = [1,5]
2>1 true
intersections=[1,2]

step 1: index = 2
current = [5,10]
2>1 true
intersections=[1,2]

"""

