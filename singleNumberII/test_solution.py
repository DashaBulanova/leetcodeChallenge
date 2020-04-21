import pytest

from singleNumberII.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [([2, 2, 3, 2], 3),
                          ([0, 1, 0, 1, 0, 1, 99], 99)])
def test_number_of_bits(input, expected):
    actual = Solution().singleNumber(input)
    assert actual == expected
