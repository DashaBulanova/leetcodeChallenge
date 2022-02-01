import pytest
from .solution import Solution

@pytest.mark.parametrize("prices, expected",[
([7,1,5,3,6,4], 5),
([7,6,4,3,1], 0)
    ])
def test(prices, expected):
    actual = Solution().maxProfit(prices)
    assert actual == expected


"""
[7,1,5,3,6,4] 
profit = 0
min_price = 7

i=1
min_price = 7
profit = max(0, -6) = 0

i=2
min_price = 1
profit = max(0, 5-1=4)=4

i=3
min_price=1
profit = max(4, 2) = 4

i=4
min_price=1
profit = max(4, 6-1) = 5

"""