class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights) # O(n log n) - time & O(n) - memory

        result = 0
        for i, v in enumerate(heights): # O(n) - time & O(1) - memory
            if v != expected[i]:
                result += 1

        return result
