import math
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = list()

        for i in range(len(mat)):
            res_row = [0] * len(mat[i])
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    continue
                else:
                    if j == 0 and i == 0:
                        res_row[j] = math.inf
                    elif j == 0:
                        res_row[j] = result[i - 1][j] + 1
                    elif i == 0:
                        res_row[j] = res_row[j - 1] + 1
                    else:
                        res_row[j] = min(result[i - 1][j] + 1, res_row[j - 1] + 1)
            result.append(res_row)

        for i in range(len(mat) - 1, -1, -1):
            for j in range(len(mat[i]) - 1, -1, -1):
                if mat[i][j] == 0:
                    continue
                else:
                    if j == len(mat[i]) - 1 and i == len(mat) - 1:
                        continue
                    elif j == len(mat[i]) - 1:
                        result[i][j] = min(result[i][j], result[i + 1][j] + 1)
                    elif i == len(mat) - 1:
                        result[i][j] = min(result[i][j], result[i][j + 1] + 1)
                    else:
                        result[i][j] = min(result[i][j], result[i + 1][j] + 1, result[i][j + 1] + 1)

        return result
