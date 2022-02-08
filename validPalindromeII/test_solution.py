import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected",[
("aba", True),
("abca", True),
("abcbja", True),
("ajbbjba", True),
("abc", False)
])
def test(input, expected):
    actual = Solution().validPalindrome(input)
    assert actual == expected
"""
ajbbjba
l,r=0,6
skipped =0

s[0]==s[6] a==a
    l=1
    r=5
s[1]!=s[5] j!=b
skipped=1
l=2

"""
