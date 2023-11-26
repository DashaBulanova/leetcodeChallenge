import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, expected", [([2, 3, 5], [4, 3, 5]), ([1, 4, 6, 8, 10], [24, 15, 13, 15, 21])]
)
def test(nums, expected):
    actual = Solution().getSumAbsoluteDifferences(nums)
    assert actual == expected
