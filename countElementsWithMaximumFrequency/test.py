import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, expected", [
	([1,2,2,3,1,4], 4),
    ([1,2,3,4,5], 5)
])
def test(nums, expected):
	actual = Solution().maxFrequencyElements(nums)
	assert actual == expected
