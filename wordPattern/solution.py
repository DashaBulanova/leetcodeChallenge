class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        r = {}
        st = s.split(" ")
        if len(st) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d:
                if st[i] != d[pattern[i]]:
                    return False
            elif st[i] in r:
                return False
            else:
                d[pattern[i]] = st[i]
                r[st[i]] = pattern[i]

        return True
