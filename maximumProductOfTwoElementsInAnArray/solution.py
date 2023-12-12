class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) < 2:
            raise ValueError()
        maxs = sorted(nums)[-2:]
        return (maxs[0]-1)*(maxs[1]-1)
        
