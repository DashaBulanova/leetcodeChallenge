class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        m = len(matrix)  # row number
        n = len(matrix[0])  # col number
        total = n * m
        rs, cs = 0, 0
        re, ce = m - 1, n - 1
        while total > 0:
            total -= self.__go(rs, re, cs, ce, matrix, result)
            rs += 1
            cs += 1
            re -= 1
            ce -= 1
        return result

    def __go(self, rs, re, cs, ce, matrix, result):
        count = 0
        for j in range(cs, ce + 1):
            result.append(matrix[rs][j])
            count += 1
        for i in range(rs + 1, re + 1):
            result.append(matrix[i][ce])
            count += 1
        if rs != re:
            for j in range(ce - 1, cs - 1, -1):
                result.append(matrix[re][j])
                count += 1
        if cs != ce:
            for i in range(re - 1, rs, -1):
                result.append(matrix[i][cs])
                count += 1
        return count
