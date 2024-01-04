import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, expected", [
    ([2,3,3,2,2,4,2,3,4], 4),
    ([2,1,2,2,3,3],-1),
    ([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12], 7),
    ([19,19,19,19,19,19,19,19,19,19,19,19,19], 5)
])
def test(nums, expected):
    actual = Solution().minOperations(nums)
    assert actual == expected
