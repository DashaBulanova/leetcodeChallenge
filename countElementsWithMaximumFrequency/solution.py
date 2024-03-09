class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        d = {}
        m = 0
        res = 0
        for i in nums:
            d[i] = d.get(i, 0)+1
            if d[i]>m:
                res = d[i]
            elif d[i]==m:
                res += d[i]
            m = max(m, d[i])
        return res
        
"""
1 d=1:1 m=1 res=1
2 d=1:1 2:1 m=1 res=2
2 d=1:1 2:2 m=2 res=2
3 d=1:1 2:2 3:1 m=2 res=2
1 d=1:2 2:2 3:1 m=2 res=4

"""