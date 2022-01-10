import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected", [
("leetcode", 0),
("loveleetcode", 2),
("aabb", -1)
    ])
def test(input, expected):
    actual = Solution().firstUniqChar(input)
    assert actual == expected