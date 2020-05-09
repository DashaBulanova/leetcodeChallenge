import pytest

from validPerfectSquare.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [(16, True),
                          (14, False),
                          (2147483648, False),
                          (2147395600, True),
                          (0, False)])
def test_number_of_bits(input, expected):
    actual = Solution().isPerfectSquare(input)
    assert actual == expected

@pytest.mark.parametrize("input, expected",
                         [(16, True),
                          (9, True),
                          (2147483648, False),
                          (2147395600, True),
                          (14, False)])
def test_number_of_bits(input, expected):
    actual = Solution().binarySearch(input)
    assert actual == expected
