import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alpha = {list(string.ascii_uppercase)[i]: i+1 for i in range(0, 26)}
        res = 0
        for i in range(len(columnTitle)):
            res = res*26+alpha[columnTitle[i]]
        return res