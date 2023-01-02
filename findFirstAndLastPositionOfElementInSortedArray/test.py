import pytest
from .solution import Solution


@pytest.mark.parametrize("nums, target, expected", [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([8, 8, 8, 8, 8, 8], 8, [0, 5]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1])
])
def test(nums, target, expected):
    actual = Solution().searchRange(nums, target)
    assert actual == expected
