class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        p1,p2=0,0

        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]==nums2[p2]:
                return nums1[p1]
            elif nums1[p1]>nums2[p2]:
                p2+=1
            else:
                p1+=1
        return -1

"""
nums1=[1,2,3,6] p1=0
nums2=[2,3,4,5] p2=0

nums1[0]=1 nums2[0]=2 => p1=1
nums1[1]=2 nums2[0]=2 = return 2

"""