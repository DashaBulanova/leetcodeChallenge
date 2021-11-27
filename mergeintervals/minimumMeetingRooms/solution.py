from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1

        start = []
        end = []
        for meeting in intervals:
            start.append(meeting[0])
            end.append(meeting[1])

        start.sort()
        end.sort()

        start_pointer = 0
        end_pointer = 0
        result, counter = 0, 0
        while start_pointer < len(start):
            if start[start_pointer] < end[end_pointer]:
                counter += 1
                result = max(result, counter)
                start_pointer += 1
            else:
                counter -= 1
                end_pointer += 1

        # TODO: Write your code here
        return result