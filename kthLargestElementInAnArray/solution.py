from typing import List
from core.dataStructure.max_heap import heapify as build_max_heap, k_largest
from core.dataStructure.min_heap import heapify as build_min_heap, k_smallest


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > int(len(nums) / 2):
            build_min_heap(nums)  # O(lgn)
            return k_smallest(nums, len(nums) - k+1)  # O(klgn)
        else:
            build_max_heap(nums)
        return k_largest(nums, k)
