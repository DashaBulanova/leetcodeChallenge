import pytest
from .solution import Solution

@pytest.mark.parametrize("n, expected",[
	(8, 6),
	(1,1),
	(4, -1)
])
def test(n, expected):
	actual = Solution().pivotInteger(n)
	assert actual == expected
