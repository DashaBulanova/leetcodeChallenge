import pytest

from coinChange2.solution import Solution


@pytest.mark.parametrize("amount, coins, expected",
                         [
                             (5, [1, 2, 5], 4),
                             (3, [2], 0),
                             (10, [10], 1),
                             (0, [], 0),
                         ])
def test_bst_to_gst(amount, coins, expected):
    actual = Solution().change(amount, coins)
    assert actual == expected
