import pytest
from .solution import Solution

@pytest.mark.parametrize("strs, expected", [
    (["flower","flow","flight"], "fl"),
    (["dog","racecar","car"], ""),
    ([""], ""),
    (["ab", "a"],"a")
])
def test(strs, expected):
    actual = Solution().longestCommonPrefix(strs)
    assert actual == expected
