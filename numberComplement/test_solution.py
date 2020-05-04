import pytest

from numberComplement.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [(5, 2),
                          (7, 0),
                          (10, 5)])
def test_number_of_bits(input, expected):
    actual = Solution().bitwiseComplement(input)
    assert actual == expected
