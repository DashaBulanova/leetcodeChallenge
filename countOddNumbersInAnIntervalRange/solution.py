class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = (high+1-low) // 2
        if (high+1-low) % 2 == 1:
            result += high % 2
        return result
