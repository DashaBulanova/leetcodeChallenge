from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #a+b+c=0 => a+b=-c
        #1. brute force => O(n^3)
        #2. O(n^2) two pointer + hashmap
        #3. sort O(nlogn) + two pointer + hashmap
        nums.sort()
        values = {}
        for i in range(len(nums)):
            if nums[i] in values:
                values[nums[i]].append(i)
            else:
                values[nums[i]] = [i]

        def twosum(s):
            res = []
            for i in range(s+1, len(nums)):
                if i>s+1 and nums[i]==nums[i-1]:
                    continue
                if -(nums[s]+nums[i]) in values:
                    for j in values[-(nums[s]+nums[i])]:
                        if j>i:
                            res.append([nums[s],nums[i],nums[j]])
                            break
            return res

        result = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue

            res = twosum(i)
            if res:
                result.extend(res)
        return result
