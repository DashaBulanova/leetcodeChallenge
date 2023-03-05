class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.__binary_search(nums, target, 0, len(nums)-1)

    def __binary_search(self, nums,target,  s, e) -> int:
        if s == e:
            if nums[s]<target:
                return s+1
            return s

        m = s+(e-s)//2
        
        if nums[m]==target:
            return m
        if nums[m]<target:
            return self.__binary_search(nums, target, m+1, e)
        else:
            return self.__binary_search(nums, target, s, m)


