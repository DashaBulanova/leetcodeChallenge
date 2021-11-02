import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
                             ([1, 3, 4, 0, 0], [1, 3, 4, 0, 0]),
                         ])
def test_number_of_bits(input, expected):
    Solution().moveZeroes(input)
    assert input == expected
