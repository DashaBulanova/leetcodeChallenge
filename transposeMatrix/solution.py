class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        result = []
        m = len(matrix) # number of rows
        n = len(matrix[0]) # numbers of columns
        result = [[0] * m for i in range(n)]
        for j in range(n):
            for i in range(m):
                result[j][i]=matrix[i][j] 
        return result
