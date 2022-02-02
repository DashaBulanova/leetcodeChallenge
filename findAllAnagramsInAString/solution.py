from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        result = []
        expected = {}
        for c in p:
            expected[c] = expected[c]+1 if c in expected else 1

        start = 0
        actual = {}
        for end in range(len(s)):
            c = s[end]
            actual[c] = actual[c]+1 if c in actual else 1
            if actual == expected:
                result.append(start)
            if end-start+1 == len(p):
                if actual[s[start]] == 1:
                    del actual[s[start]]
                else:
                    actual[s[start]] -= 1
                start += 1

        return result

