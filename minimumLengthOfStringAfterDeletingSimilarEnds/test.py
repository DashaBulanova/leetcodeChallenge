import pytest
from .solution import Solution

@pytest.mark.parametrize("s, expected",[
	("ca", 2),
	("cabaabac", 0),
	("aabccabba", 3)
])
def test(s, expected):
	actual = Solution().minimumLength(s)
	assert actual == expected
