
import pytest
from .solution import Solution

@pytest.mark.parametrize("input, target, expected", [
([4,5,6,7,0,1,2], 0, 4),
([4,5,6,7,0,1,2], 3, -1),
([], 0, -1),
([3,5,1], 3, 0),
([5,1,3], 5, 0),
([4,5,6,7,8,1,2,3],8,4),
([3,1],1, 1)
    ])
def test(input, target, expected):
    actual = Solution().search(input, target)
    assert actual == expected


"""
[4,5,6,7,0,1,2], target=0
0,6
mid = 3
mid_item=7

4<7<

"""