import pytest

from .solution import Solution


@pytest.mark.parametrize("input, target, expected",
                         [
                             ([2, 7, 11, 15], 9, [1, 2]),
                             ([2, 3, 4], 6, [1, 3]),
                             ([-1,0], -1, [1,2]),
                         ])
def test_number_of_bits(input, target, expected):
    actual = Solution().twoSum(input, target)
    assert actual == expected
