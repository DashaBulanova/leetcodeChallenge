import pytest

from bestTimeToBuyAndSellStock.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [([7, 1, 5, 3, 6, 4], 5),
                          ([7, 6, 4, 3, 1], 0)])
def test_number_of_bits(input, expected):
    actual = Solution().maxProfit(input)
    assert actual == expected
