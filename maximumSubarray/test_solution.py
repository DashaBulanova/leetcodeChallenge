import pytest

from maximumSubarray.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)])
def test_number_of_bits(input, expected):
    actual = Solution().maxSubArray(input)
    assert actual == expected
