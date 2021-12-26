import pytest
from .solution import search_rotated_array

@pytest.mark.parametrize("input, target, expected", [
    ([1, 3, 8, 10, 15], 10, 3),
    ([10, 15, 1, 3, 8], 15, 1),
    ([4, 5, 7, 9, 10, -1, 2], 10, 4),
    ([15, 10, 8, 3, 1], 15, 0),
    ([4,5,6,7,0,1,2],0,4),
    ([3,1], 1, 1)
    ])
def test(input, target, expected):
    actual = search_rotated_array(input, target)
    assert actual == expected

"""
[3,1]
0,1
mid=0


[4, 5, 7, 9, 10, -1, 2] key=0
0,6
mid=3
9==0 false
4<9 sorted=> true
    4<=0<9 false=>
        start = 4

mid=4+1=5
10<-1 false
10<0<=2 false
end=5

4,5
mid=4+1/2=4
10<0<=
0<9

[4,5,6,7,0,1,2] key=0
0,6
mid-3
4<7 true
    4<=0<
"""