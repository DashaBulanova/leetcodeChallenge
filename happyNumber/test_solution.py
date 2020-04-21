import pytest

from happyNumber.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [(19, True),
                         (17, False)])
def test_number_of_bits(input, expected):
    actual = Solution().isHappy(input)
    assert actual == expected
