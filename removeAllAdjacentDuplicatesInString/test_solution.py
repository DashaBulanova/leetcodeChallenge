import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected",
	[("abbaca", "ca"),
	("azxxzy", "ay")])
def test(input, expected):
	actual = Solution().removeDuplicates(input)
	assert actual == expected