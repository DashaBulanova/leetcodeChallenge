from typing import List

from core.dataStructure.max_heap import heapify, k_largest


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        return k_largest(nums, k)