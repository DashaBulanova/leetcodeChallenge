import string
from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:

        chars = dict()
        for i in range(0, len(s)):
            c = s[i]
            if c not in chars:
                chars[c] = 0
            chars[c] += 1

        result = ""
        for key, value in reversed(sorted(chars.items(), key=lambda x: x[1])):
            result += value * key

        return result
