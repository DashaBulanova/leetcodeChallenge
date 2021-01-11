import pytest

from uglyNumberII.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             (10, 12),
                             (22, 45),
                             (1,1),
                             (309, 96000),
                             (424, 409600)
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().nthUglyNumber(input)
    assert actual == expected


