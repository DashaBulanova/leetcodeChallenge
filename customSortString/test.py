import pytest
from .solution import Solution

@pytest.mark.parametrize("order, s, expected", [
	("cba", "abcd", "cbad"),
	("bcafg","abcd", "bcad"),
	("kqep","pekeq", "kqeep")
])
def test(order, s, expected):
	actual = Solution().customSortString(order, s)
	assert actual == expected
