import pytest

from numberOf1Bits.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [(0b00000000000000000000000000001011, 3),
                          (0b00000000000000000000000010000000, 1),
                          (0b11111111111111111111111111111101, 31)])
def test_number_of_bits(input, expected):
    actual = Solution().hammingWeight(input)
    assert actual == expected
