from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s = self.define_pointer(intervals, newInterval[0], 0, len(intervals) - 1)
        e = self.define_pointer(intervals, newInterval[1], 0, len(intervals) - 1)

        result = []
        if s == -1 and e > len(intervals) - 1:
            result.append([newInterval[0], newInterval[1]])
        elif s == -1 and e == -1:
            result.append([newInterval[0], newInterval[1]])
            result.extend(intervals)
        elif s > len(intervals) - 1 and e > len(intervals) - 1:
            result.extend(intervals)
            result.append([newInterval[0], newInterval[1]])
        elif s == -1:
            result.append([newInterval[0], max(intervals[e][1], newInterval[1])])
            result.extend(intervals[e + 1:len(intervals)])
        elif e > len(intervals) - 1:
            if intervals[s][1] < newInterval[0]:
                s = s + 1
            result.extend(intervals[0:s])
            result.append([min(intervals[s][0], newInterval[0]), newInterval[1]])
        else:
            if intervals[s][1] < newInterval[0]:
                s = s + 1
            result.extend(intervals[0:s])
            result.append([min(intervals[s][0], newInterval[0]), max(intervals[e][1], newInterval[1])])
            result.extend(intervals[e + 1:len(intervals)])
        return result

    # return pointer in intervals where point >= si
    def define_pointer(self, intervals: List[List[int]], value, s, e) -> int:

        if s == e:
            if intervals[s][0] <= value <= intervals[s][1]:
                return s
            if value < intervals[s][0]:
                return s - 1
            if value > intervals[s][1]:
                return s + 1

        if e < s:
            return -1

        m = s + (e - s) // 2
        if intervals[m][0] == value:
            return m

        if value < intervals[m][0]:
            return self.define_pointer(intervals, value, s, m)
        else:
            index = self.define_pointer(intervals, value, m + 1, e)
            return index
