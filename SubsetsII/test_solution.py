import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             # ([0], [[], [0]]),
                             ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().subsetsWithDup(input)
    assert actual == expected
