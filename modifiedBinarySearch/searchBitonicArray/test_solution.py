import pytest

from .solution import search_bitonic_array


@pytest.mark.parametrize("input, target, expected", [
    ([1, 3, 8, 4, 3], 4, 3),
    ([1, 3, 8, 12], 12, 3),
    ([1, 3, 8, 12], 9, -1),
    ([10, 9, 8], 10, 0),
    ([3, 8, 3, 1], 8, 1)])
def test(input, target, expected):
    actual = search_bitonic_array(input, target)
    assert actual == expected


"""
[1, 3, 8, 4, 3] target = 4

0,4
0==4 False
mid=2
8==4 false

left => -1
    0,2
    mid=1
    left=> 0,1 => -1
        mid=0
        left => 0,0 return -1
        right=>1,1 return -1
    right=> 2,2 => -1
rigth => 3
    3,4
    mid = 3
    4==4 return 3
return 3


[1, 3, 8, 12] key=12
0,3
mid=1
12==3 False
left => 0,1=>-1
    mid=0
    left=>0,0 => -1
    right=>1,1=>-1
right => 2,3 => 3
    mid = 2
    left=> 2,2 => -1
    right=>3,3=>3

"""
