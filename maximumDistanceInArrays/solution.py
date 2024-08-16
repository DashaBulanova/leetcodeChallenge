class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        m = len(arrays)
        maxs = []
        mins = []
        for i in range(len(arrays)):
            mins.append((arrays[i][0], i))
            maxs.append((arrays[i][len(arrays[i]) - 1], i))

        mins.sort()
        maxs.sort(reverse=True)

        if mins[0][1] != maxs[0][1]:
            return abs(mins[0][0] - maxs[0][0])
        else:
            return max(abs(mins[0][0] - maxs[1][0]), abs(mins[1][0] - maxs[0][0]))
