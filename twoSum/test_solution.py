import pytest

from .solution import Solution


@pytest.mark.parametrize("input, target, expected",
                         [
                             ([2, 7, 11, 15], 9, [0, 1]),
                             ([3, 2, 4], 6, [1, 2]),
                             ([3, 3], 6, [0, 1]),
                             ([3, 2, 3], 6, [0, 2]),
                             ([2, 5, 5, 11], 10, [1, 2]),
                         ])
def test_number_of_bits(input, target, expected):
    actual = Solution().twoSum(input, target)
    assert actual == expected
