import pytest
from .solution import Solution

@pytest.mark.parametrize("nums1, nums2, expected", [
	([1,2,2,1], [2,2], [2]),
	([4,9,5], [9,4,9,8,4], [9,4])
])
def test(nums1, nums2, expected):
	actual = Solution().intersection(nums1, nums2)
	assert actual == expected
