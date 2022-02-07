class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        expected = {}
        for i in range(len(t)):
            expected[t[i]]=expected.get(t[i], 0)+1
            if i<len(t)-1:
                expected[s[i]]=expected.get(s[i], 0)-1

        for key,value in expected.items():
            if value > 0:
                return key

        raise ValueError()