class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums)):
            int_res = self._max_length(i, nums)
            res = max(res, int_res)

        return res

    def _max_length(self, s, nums)->int:
        ones=nums[s]
        zeros=1 if nums[s]==0 else 0 
        res = 0
        for e in range(s+1,len(nums),1):
            ones+=nums[e]
            if nums[e] == 0:
                zeros+=1

            if ones == zeros:
                res=e-s+1
        return res

"""
[0,1]
s=0
max_length=>2
    ones=0
    zeros=1
    j=1
    ones=1
    res=1-0+1=2
s=1
max_length=>
    ones=1
    zeros=0
    j=1
"""     