class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        s,e=0,len(nums)-1

        d=set()
        result=0
        while s<=e:
            if nums[s] not in d:
                d.add(nums[s])
                s+=1
            else:
                nums[s]+=1
                result+=1
            if s<e:
                if nums[e] not in d:
                    d.add(nums[e])
                    e-=1
                else:
                    nums[e]+=1
                    result+=1
        return result
