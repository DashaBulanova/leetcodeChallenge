import pytest
from .solution import Solution 

@pytest.mark.parametrize("input, k, expected", [
("abcd", 2, "abcd"),
("deeedbbcccbdaa", 3, "aa"),
("pbbcggttciiippooaais", 2, "ps")
])
def test(input, k, expected):
	actual = Solution().removeDuplicates(input, k)
	assert actual == expected
