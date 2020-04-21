import pytest

from singleNumber.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [([2, 2, 1], 1),
                          ([4, 1, 2, 1, 2], 4)])
def test_number_of_bits(input, expected):
    actual = Solution().singleNumber(input)
    assert actual == expected
