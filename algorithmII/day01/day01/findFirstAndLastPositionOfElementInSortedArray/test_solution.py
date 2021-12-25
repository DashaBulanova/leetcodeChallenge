import pytest
from .solution import Solution

@pytest.mark.parametrize("input, target, expected", [
([5,7,7,8,8,10], 8, [3,4]),
([5,7,7,8,8,10], 6, [-1,-1]),
([], 6, [-1,-1])
	])
def test(input, target, expected):
	actual = Solution().searchRange(input, target)
	assert actual == expected