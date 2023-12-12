import pytest
from .solution import Solution

@pytest.mark.parametrize("nums,expected", [
([3,4,5,2],12),
([1,5,4,5], 16),
([3,7],12)
])
def test(nums,expected):
    actual = Solution().maxProduct(nums)
    assert actual == expected
