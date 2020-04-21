import pytest

from divideTwoIntegers.solution import Solution


@pytest.mark.parametrize("dividend, divisor, expected",
                         [
                           (52, 3, 17),
                           (2147483647, 2, 1073741823),
                           (-2147483648, -1, 2147483647),
                           (-2147483648, 1, -2147483648),
                           (2147483647, 1, 2147483647),
                           (1, 1, 1),
                           (-1, -1, 1),
                           (1, -1, -1),
                           (10, 3, 3),
                           (7, 3, 2),
                           (7, -3, -2)
                         ])
def test_number_of_bits(dividend, divisor, expected):
    actual = Solution().divide(dividend, divisor)
    assert actual == expected
