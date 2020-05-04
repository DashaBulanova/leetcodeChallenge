import pytest

from uglyNumber.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [(6, True),
                          (8, True),
                          (0, False),
                          (14, False)])
def test_number_of_bits(input, expected):
    actual = Solution().isUgly(input)
    assert actual == expected
