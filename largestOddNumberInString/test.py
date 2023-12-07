import pytest
from .solution import Solution

@pytest.mark.parametrize("num, expected", [
("52", "5"),
    ("4206", ""),
    ("35427", "35427"),
])
def test(num, expected):
	actual = Solution().largestOddNumber(num)
	assert actual == expected
