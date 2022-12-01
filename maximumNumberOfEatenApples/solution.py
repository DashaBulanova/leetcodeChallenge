from typing import List
from heapq import heapify, heappush, heappop, heapreplace


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        result = 0
        i = 0
        heap = []
        heapify(heap)
        while i < len(apples) or len(heap):
            if i < len(days) and days[i] > 0:
                heappush(heap, (days[i] + i, apples[i]))
            if len(heap):
                result += 1
                heapreplace(heap, (heap[0][0], heap[0][1] - 1))
                while len(heap) and (heap[0][1] == 0 or heap[0][0] == i + 1):
                    heappop(heap)
            i += 1
        return result
