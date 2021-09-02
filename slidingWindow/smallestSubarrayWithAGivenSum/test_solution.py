import pytest

from .solution import Solution


@pytest.mark.parametrize("input, s, expected",
                         [
                             ([2, 1, 5, 2, 3, 2], 7, 2),
                             ([2, 1, 5, 2, 8], 7, 1),
                             ([3, 4, 1, 1, 6], 8, 3),
                         ])
def test_number_of_bits(input, s, expected):
    actual = Solution().smallest_subarray_with_given_sum(s, input)
    assert actual == expected
