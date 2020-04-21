import pytest

from contiguousArray.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [([0, 1], 2),
                          ([0, 1, 0], 2),
                          ([0, 1, 1, 0], 4),
                          ([0, 1, 1, 0, 1, 1, 1, 0], 4),
                          ([0, 0, 1, 0, 0, 0, 1, 1], 6)])
def test_number_of_bits(input, expected):
    actual = Solution().findMaxLength(input)
    assert actual == expected
