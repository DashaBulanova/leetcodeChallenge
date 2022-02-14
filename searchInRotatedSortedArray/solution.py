from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        def binarySearch(s,e)->int:
            if s==e:
                return s if nums[s] == target else -1

            #[4,5,6,7,0,1,2]
            #
            mid=s+(e-s)//2
            if nums[mid]==target:
                return mid

            if nums[s]<=nums[mid]:
                if nums[s]<=target<nums[mid]:
                    return binarySearch(s, mid)
                else:
                    return binarySearch(mid+1, e)
            else:
                if nums[mid]<target<=nums[e]:
                    return binarySearch(mid+1, e)
                else:
                    return binarySearch(s, mid)

        return binarySearch(0, len(nums)-1)