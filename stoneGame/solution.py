from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alex = 0
        lee = 0
        is_alex = True
        for i in range(len(piles)):
            if is_alex:
                alex += max(piles[i], piles[len(piles)-1-i])
            else:
                lee += max(piles[i], piles[len(piles)-1-i])
        return alex > lee
