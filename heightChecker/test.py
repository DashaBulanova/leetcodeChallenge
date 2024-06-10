import pytest

from .solution import Solution

@pytest.mark.parametrize("heights, expected", [
	([1,1,4,2,1,3], 3),
	([5,1,2,3,4], 5),
	([1,2,3,4,5], 0)
])
def tests(heights, expected):
	actual = Solution().heightChecker(heights)
	assert actual == expected
