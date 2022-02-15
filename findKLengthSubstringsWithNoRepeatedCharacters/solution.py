class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        hashmap = {}
        result = 0
        start = 0
        for end in range(len(s)):
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if end - start + 1 == k:
                if all(val == 1 for val in hashmap.values()):
                    result += 1
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                start += 1
        return result
