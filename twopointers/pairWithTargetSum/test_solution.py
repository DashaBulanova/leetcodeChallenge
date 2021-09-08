import pytest

from .solution import Solution


@pytest.mark.parametrize("input, target, expected",
                         [
                             ([1, 2, 3, 4, 6], 6, [1, 3]),
                             ([2, 5, 9, 11], 11, [0, 2]),
                         ])
def test_number_of_bits(input, target, expected):
    actual = Solution().pair_with_targetsum(input, target)
    assert actual == expected
