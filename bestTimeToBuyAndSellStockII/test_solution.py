import pytest

from bestTimeToBuyAndSellStockII.solution import Solution


@pytest.mark.parametrize("input, expected",
                         [
                             ([7, 1, 5, 3, 6, 4], 7),
                             ([1, 2, 3, 4, 5], 4),
                             ([7, 6, 4, 3, 1], 0),
                             ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 15)])
def test_number_of_bits(input, expected):
    actual = Solution().maxProfit(input)
    assert actual == expected
