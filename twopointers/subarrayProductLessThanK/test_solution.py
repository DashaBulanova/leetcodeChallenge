import pytest

from .solution import Solution


@pytest.mark.parametrize("input, target, expected",
                         [
                             ([10, 5, 2, 6], 100, 8),
                             ([2, 5, 3, 10], 30, 6),
                             ([1, 2, 3], 0, 0),
                             ([1, 1, 1], 1, 0),
                             ([10, 2, 2, 5, 4, 4, 4, 3, 7, 7], 289, 31),
                             ([57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75, 22], 18, 1),
                             ([100, 2, 3, 4, 100, 5, 6, 7, 100], 100, 11)
                         ])
def test(input, target, expected):
    actual = Solution().numSubarrayProductLessThanK(input, target)
    assert actual == expected
