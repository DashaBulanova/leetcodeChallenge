class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]*45
        for i in range(1, n+1):
            if i == 1:
                res[i-1] = 1
            elif i == 2:
                res[i-1] = 2
            else:
                res[i-1] = res[i-2] + res[i-3]
        return res[n-1]

"""
i = 1 2 3 4 5
    1 2 3 5 8
in  0 1 2 3 4

1 + 1 + 1+ 1
2 + 2
1 + 2 + 1
1 + 1 + 2
2 + 1 + 1
"""
