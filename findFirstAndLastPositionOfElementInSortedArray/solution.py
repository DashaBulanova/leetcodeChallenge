class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0:
            return [-1, -1]
        return self.__searchRange(0, len(nums)-1, nums, target)

    def __searchRange(self, s, e, nums: list[int], target: int) -> list[int]:
        if s == e:
            return [s, s] if nums[s] == target else [-1, -1]

        m = s + (e-s) // 2
        if target < nums[m]:
            return self.__searchRange(s, m, nums, target)

        if target > nums[m]:
            return self.__searchRange(m+1, e, nums, target)

        l = self.__searchRange(s, m, nums, target)
        r = self.__searchRange(m+1, e, nums, target)

        return [r[0] if l[0] == -1 else l[0], max(l[1], r[1])]


"""
[5, 7, 7, 8, 8, 10] t=8
s=0,e=5
m=0+5//2=2
nums[2]==7

s=3, e=5
m=5-3=2//2=1+3=4
l=search(3,4)=>
    m=3+
r=search(4,4)=>[4,4]
"""
