import math


def isBadVersion(n: int) -> bool:
    if n == 3:
        return False
    if n == 4:
        return True
    if n == 5:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        candidate = math.inf
        while start <= end:
            index = start + int((end - start) / 2)
            if not isBadVersion(index):
                start = index + 1
            else:
                candidate = min(candidate, index)
                end = index - 1
        return candidate
