class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        if len(strs) == 0:
            return 0
        result = 0
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if strs[i][j] < strs[i-1][j]:
                    result += 1
                    break

        return result
