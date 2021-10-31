import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             (5, 4),
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().firstBadVersion(input)
    assert actual == expected
