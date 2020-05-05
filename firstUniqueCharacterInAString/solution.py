import string
from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:

        chars = dict()
        for i in range(0, len(s)):
            c = s[i]
            if s[i] not in chars:
                chars[c] = []

            chars[c].append(i)

        for key, value in chars.items():
            if len(value) == 1:
                return int(value[0])

        return -1
