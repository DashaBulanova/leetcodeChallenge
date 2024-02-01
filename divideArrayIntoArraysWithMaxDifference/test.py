import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, k, expected", [
	# ([1,3,4,8,7,9,3,5,1], 2, [[1,1,3],[3,4,5],[7,8,9]]),
	# ([1,3,3,2,7,3],3,[]),
	([33,26,4,18,16,24,24,15,8,18,34,20,24,16,3], 16,[[3,4,8],[15,16,16],[18,18,20],[24,24,24],[26,33,34]] )
])
def test(nums, k, expected):
	actual = Solution().divideArray(nums, k)
	assert actual == expected

