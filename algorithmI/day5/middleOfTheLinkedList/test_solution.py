import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
                             (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
                         ])
def test_number_of_bits(input, expected):
    Solution().reverseString(input)
    assert input == expected
