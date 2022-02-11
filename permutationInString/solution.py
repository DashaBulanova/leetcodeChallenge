class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        expected = {}
        for s in s1:
            expected[s] = expected.get(s, 0) + 1

        actual = {}
        start = 0
        for end in range(len(s2)):
            actual[s2[end]] = actual.get(s2[end], 0) + 1
            if actual == expected:
                return True

            if end - start + 1 == len(s1):
                actual[s2[start]] -= 1
                if actual[s2[start]] == 0:
                    del actual[s2[start]]
                start += 1

        return False
