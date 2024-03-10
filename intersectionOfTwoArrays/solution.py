class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) >= len(set2):
            return list(set1.intersection(set2))
        else:
            return list(set2.intersection(set1))