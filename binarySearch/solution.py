class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.__search(nums, target, 0, len(nums)-1)
    
    def __search(self, nums: list[int], target: int, s: int ,e: int) -> int:
        if s == e:
            if nums[s] == target: 
                return s
            else:
                return -1

        mid = s + (e-s)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.__search(nums, target, mid+1, e)
        else:
            return self.__search(nums, target, s, mid)
