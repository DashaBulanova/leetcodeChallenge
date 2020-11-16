from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        sorted_coins = sorted(coins)

        prev = [0] * (amount+1)
        for coin in sorted_coins:
            for i in range(0, amount+1):
                if i == 0:
                    prev[i] = 1
                elif coin > i:
                    prev[i] = prev[i]
                else:
                    prev[i] = prev[i] + prev[i - coin]

        return prev[amount]