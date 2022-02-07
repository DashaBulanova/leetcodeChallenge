import pytest
from .solution import Solution

@pytest.mark.parametrize("s,t, expected", [
    ("abcd", "abcde", "e"),
    ("","y", "y")
])
def test(s,t, expected):
    actual = Solution().findTheDifference(s,t)
    assert actual == expected