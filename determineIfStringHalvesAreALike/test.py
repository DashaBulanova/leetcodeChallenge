import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected",[
("book", True),
("textbook", False)
])
def test(input, expected):
	actual = Solution().halvesAreAlike(input)
	assert actual == expected
