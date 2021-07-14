import pytest

from findPeakElement.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                          ([1, 2, 3, 1], 3),
                          ([1, 2, 1, 3, 5, 6, 4], 6),
                          ([1], 1),
                          ([1, 2], 2)])
def test_number_of_bits(input, expected):
    actual = Solution().findPeakElement(input)
    assert actual == expected
