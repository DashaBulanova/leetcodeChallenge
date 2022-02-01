from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(prices[i-1], min_price)
            profit = max(profit, prices[i] - min_price)

        return profit