import re


class Solution(object):
    def reverseWords(self, s):
        trimmed = s.strip()+' '
        regex = r"(\S.*?\s)"

        matches = list(re.finditer(regex, trimmed, re.MULTILINE))

        len(matches)
        result = ''
        for match in reversed(matches):
            result += match.group()

        return result.strip()
