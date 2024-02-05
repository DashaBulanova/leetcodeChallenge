import pytest
from .solution import Solution

@pytest.mark.parametrize("s, expected", [
	("leetcode", 0),
	("loveleetcode", 2),
	("aabb", -1)
])
def test(s, expected):
	actual = Solution().firstUniqChar(s)
	assert actual == expected
