
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap[c] + 1 if c in hashmap else 1

        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1