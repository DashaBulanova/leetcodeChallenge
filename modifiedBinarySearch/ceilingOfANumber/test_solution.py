"""
[4, 6, 10], key = 6, 1
[1, 3, 8, 10, 15, 17], key = 12, 4
[4, 6, 10], key = 17, -1
[4, 6, 10], key = -1, 0
"""

"""
[1, 3, 8, 10, 15, 17], 12

find_ceiling(0, 5)
i=0 j=5
mid = 0+5/2=2
mid_item=8

return find_ceiling(3, 5)->
    i=3 j=5
    mid = 3+int(5-2)/2=4
    mid_item=15
    15>12 True
    return min(15, find_ceiling(3,4) -> 
        i=3, j=4
        mid = 3
        mid_item=10
        return find_ceiling(4,4) -> math.inf) -> 15

"""

"""
[4, 6, 10], key = 17, -1

i=0, j=2
mid = 1
mid_item=6
#go right
return find_ceiling(2, 2) -> -1
"""

"""
[4, 6, 10], key = -1, 0

i=0, j=2
mid = 1
mid_item=6
#go_left
left = find_ceiling(0, 1) ->
    i=0, j=1
    mid=0
    mid_item = 4
    4 > -1
    go left

"""

import pytest
from solution import ceiling

@pytest.mark.parametrize("input, target, expected", [
    ([4, 6, 10], 6, 1),
    ([1, 3, 8, 10, 15, 17], 12, 4),
    ([4, 6, 10], 17, -1),
    ([4, 6, 10], -1, 0)
    ])
def test(input, target, expected):
    assert ceiling(input, target) == expected