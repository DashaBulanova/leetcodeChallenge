import heapq


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)

        for i in range(k):
            item = heapq.heappop(piles)
            heapq.heappush(piles, item // 2)

        return -sum(piles)
