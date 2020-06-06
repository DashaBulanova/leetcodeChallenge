import pytest

from maximumSumCircularSubarray.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([1, -2, 3, -2], 3),
                             ([5, -3, 5], 10),
                             ([3, -2, 2, -3], 3),
                             ([-2, -3, -1], -1),
                         ])
def test_number_of_bits(input, expected):
    actual = Solution().maxSubArray(input)
    assert actual == expected
