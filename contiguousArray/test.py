import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, expected",[
	([0,1], 2),
	([1,0,0,1,0,1],6),
	([1,0,1,1,0,0,0,0],6),
	([0,0,1,1,0,0,0,0],4)
])
def test(nums, expected):
	actual = Solution().findMaxLength(nums)
	assert actual == expected
"""
[1,0,0,1,0,1] = 6
[1,0,0,1,0,0] = 4
[0,0,0,1,0,1] = 4
[1,0,1,1,0,0,0,0]

[1,0,1,1,0,0,0,0,1,1,1,1]

brute force

"""