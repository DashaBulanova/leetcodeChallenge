from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            max_profit += max(profit, 0)

        return max_profit
