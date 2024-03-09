import pytest
from .solution import Solution

@pytest.mark.parametrize("nums1, nums2, expected",[
	([1,2,3], [2,4], 2),
	([6,7], [2,3,4,5], -1)
])
def test(nums1, nums2, expected):
	actual = Solution().getCommon(nums1, nums2)
	assert actual == expected
