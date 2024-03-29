import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, expected",[
	([-4,-1,0,3,10], [0,1,9,16,100]),
	([-7,-3,2,3,11], [4,9,9,49,121])
])
def test(nums, expected):
	actual = Solution().sortedSquares(nums)
	assert actual == expected
