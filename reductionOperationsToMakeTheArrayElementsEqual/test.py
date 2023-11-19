import pytest
from .solution import Solution


@pytest.mark.parametrize("nums, expected", [
    ([5, 1, 3], 3),
    ([1, 1, 2, 2, 3], 4),
    ([1,1,1], 0)
])
def test(nums, expected):
    actual = Solution().reductionOperations(nums)
    assert actual == expected
