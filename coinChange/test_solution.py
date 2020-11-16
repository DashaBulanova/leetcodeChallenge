import pytest

from coinChange.solution import Solution


@pytest.mark.parametrize("amount, coins, expected",
                         [
                         #    (11, [1, 2, 5], 3),
                        #     (3, [2], -1),
                             (6349, [186, 419, 83, 408], 20),
                         #    (0, [1], 0),
                         ])
def test_change_coin(amount, coins, expected):
    actual = Solution().coinChange(coins, amount)
    assert actual == expected
