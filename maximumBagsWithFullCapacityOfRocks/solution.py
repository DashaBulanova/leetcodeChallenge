class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        n = len(capacity)
        res = 0
        needs = [0]*n
        for i in range(n):
            needs[i] = capacity[i] - rocks[i]
            if needs[i] == 0:
                res += 1

        if res == n:
            return res

        needs.sort()
        for i in range(res, n):
            additionalRocks -= needs[res]
            if additionalRocks >= 0:
                res += 1
        return res
