from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashsum = {}
        for a in nums1:
            for b in nums2:
                hashsum[a+b] = hashsum.get(a+b,0)+1 

        result = 0
        for c in nums3:
            for d in nums4:
                result += hashsum.get(-(c+d), 0)

        return result
