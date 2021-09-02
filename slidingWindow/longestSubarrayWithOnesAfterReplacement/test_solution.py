import pytest

from .solution import Solution


@pytest.mark.parametrize("input, s, expected",
                         [
                             ([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2, 6),
                             ([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3, 9),
                         ])
def test_number_of_bits(input, s, expected):
    actual = Solution().length_of_longest_substring(input, s)
    assert actual == expected
