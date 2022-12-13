import math


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        res = matrix[0]
        for r in range(1, n):
            rr = [0]*n
            for c in range(n):
                dl, dr = math.inf, math.inf
                if c != 0:
                    dl = matrix[r][c]+res[c-1]
                if c != n-1:
                    dr = matrix[r][c]+res[c+1]
                ab = matrix[r][c]+res[c]
                rr[c] = min([dl, ab, dr])
            res = rr

        return min(res)


"""
n=3
res=[2,1,3]

r=1, c=0
dl,dr=0,0
dr=2+5=7,ab=8
res[0]=min(7,8)=7

r=1,c=1
dl=7,dr=5,ab=6 res[1]=5

r=1,c=2
dl=8, ab=7 res[2]=7

r=2, c=0
dr=14, ab15 res[0]=14

r=2, c=1
dr=12,
"""
