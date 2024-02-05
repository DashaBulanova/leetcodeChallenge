class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = (d[s[i]][0]+1, i)
            else:
                d[s[i]] = (1,i)

        for k,v in d.items():
            if v[0]==1:
                return v[1]
        return -1