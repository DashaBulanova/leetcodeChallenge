import pytest
from .solution import Solution


@pytest.mark.parametrize("costs, coins, expected", [
    ([1, 3, 2, 4, 1], 7, 4),
    ([10, 6, 8, 7, 7, 8], 5, 0),
    ([1, 6, 3, 1, 2, 5], 20, 6)
])
def test(costs, coins, expected):
    actual = Solution().maxIceCream(costs, coins)
    assert actual == expected
