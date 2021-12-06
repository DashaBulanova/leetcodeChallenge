"""
[6, 6, 6, 6, 6] key = 4
[4, 6, 6, 6, 9], key = 4, [1,3]
[4, 6, 6, 6, 9] start = 0, end=0

start=
"""


"""
[4, 6, 6, 6, 9] 4

0, 4
mid=2
mid_item = 6

6>4 => find(0, 1) ->
    mid = 0
    mid_item = 4
    right = find(1,1)->[1,1]
    left = find(0, -1)->[-1,-1]
    return 0, 1

"""

import pytest
from solution import find_key_range

@pytest.mark.parametrize("input, target, expected", [
    ([6, 6, 6, 6, 6], 6, [0,4]),
    ([4, 6, 6, 6, 9], 4 , [0,0]),
    ([1, 3, 8, 10, 15], 10, [3,3]),
    ([1, 3, 8, 10, 15], 12, [-1, -1])
    ])
def test(input, target, expected):
    assert find_key_range(input, target) == expected