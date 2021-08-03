from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)): #O(n)
            if nums[i] in dic:
                value = dic[nums[i]]
                value.append(i)
            else:
                dic[nums[i]] = [i]

        for i in range(len(nums)):  #O(n)+0{n)
            if target - nums[i] in dic:
                second_values = dic[target - nums[i]]
                for j in second_values:  #O(n*m) where m is count of duplicated elenemnt
                    if i != j:
                        return [i, j]
