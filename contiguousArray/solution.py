class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        d={0:-1}
        res = 0
        sums=0
        for i in range(len(nums)):
            sums += -1 if nums[i]==0 else 1
            if sums in d:
                res=max(res, i-d[sums])
            else:
                d[sums]=i
        return res

"""
[0,1,0,1]
res=0
1. i=0 sums=-1 d={-1:0}
2. i=1 sums=0 res=2 d={-1:0,0:-1}
3. i=2 sums=-1 res=2 d={-1:2,0:1}
4. i=3 sums=0 res=2 d={-1:2,0:1}
"""     