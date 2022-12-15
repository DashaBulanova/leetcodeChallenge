class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        d = [[0] * len(text1) for i in range(len(text2))]
        for i in range(len(d)):
            for j in range(len(d[i])):
                if text1[j] == text2[i]:
                    if i > 0 and j > 0:
                        d[i][j] = d[i - 1][j - 1] + 1
                    else:
                        d[i][j] = 1
                else:
                    if i > 0 and j > 0:
                        d[i][j] = max(d[i - 1][j], d[i][j - 1])
                    elif i > 0:
                        d[i][j] = d[i - 1][j]
                    elif j > 0:
                        d[i][j] = d[i][j - 1]
                    else:
                        d[i][j] = 0
        return d[len(text2) - 1][len(text1) - 1]
