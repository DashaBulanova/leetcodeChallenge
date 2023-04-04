class Solution:
    def partitionString(self, s: str) -> int:
        frequency = set()
        result = 1
        for c in s:
            if c in frequency:
                frequency = set()
                result += 1
            frequency.add(c)
        return result

