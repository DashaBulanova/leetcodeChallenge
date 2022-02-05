from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # ["a","a","b","b","c","c","c"]
        # e         |
        # s         |
        # i         |
        start, insert, count = 0, 0, 0

        def compress_char(i, char, count) -> int:
            chars[i] = char
            if count > 1:
                for c in str(count):
                    i += 1
                    chars[i] = c
            return i+1

        for end in range(0, len(chars)):
            if chars[end] == chars[start]:
                count += 1
            else:
                insert = compress_char(insert, chars[start], count)
                count = 1
                start = end

        insert = compress_char(insert, chars[start], count)
        del chars[insert:len(chars)]
        return len(chars)
