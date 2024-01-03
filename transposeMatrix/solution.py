class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        result = []
        m = len(matrix) # number of rows
        n = len(matrix[0]) # numbers of columns
        result = [[matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]
        return result
