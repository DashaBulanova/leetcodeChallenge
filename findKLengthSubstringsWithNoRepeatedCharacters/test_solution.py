import pytest

from .solution import Solution


@pytest.mark.parametrize("input, k, expected", [
    ("havefunonleetcode", 5, 6),
    ("home", 5, 0)
])
def test(input, k, expected):
    actual = Solution().numKLenSubstrNoRepeats(input, k)
    assert actual == expected


"""
 01234567890123456
 havefunonleetcode
s            |
e                |
e=0 h={t:1,c:1,o:1,d:1,e:1}
res=5
"""
