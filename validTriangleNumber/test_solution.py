import pytest

from .solution import Solution

@pytest.mark.parametrize("input, expected",
                         [
                             ([2, 2, 3, 4], 3),
                             ([4, 2, 3, 4], 4)
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().triangleNumber(input)
    assert actual == expected
