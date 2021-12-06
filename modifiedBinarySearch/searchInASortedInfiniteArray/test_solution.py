"""
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
[1, 3, 8, 10, 15], key = 15


"""

"""
[1, 3, 8, 10, 15], 15
n=0
start = 0 end=1
mid = 0
mid_item=1
start = 1
end = 2

mid = 1
mid_item =3
start = 2
n=2
end=4

mid = 2+1=3
mid_item =10
start = 4
n=3
end=8

mid = 4+2=6
mid_item =inf
end = int(2^2.5)=5

mid = 4+(5-2)/2=5
mid_item =inf
end =4




"""


import pytest
from solution import search_in_infinite_array, ArrayReader

@pytest.mark.parametrize("input, target, expected", [
    ([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 16, 6),
    ([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], 11, -1),
    ([1, 3, 8, 10, 15], 15, 4),
    ([1, 3, 8, 10, 15], 200, -1)
    ])
def test(input, target, expected):
    assert search_in_infinite_array(ArrayReader(input), target) == expected
