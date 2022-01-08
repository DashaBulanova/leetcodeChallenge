import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected",[
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1],1)
])
def test(input, expected):
    actual = Solution().maxArea(input)
    assert actual == expected

"""
[1,8,6,2,5,4,8,3,7]
start =0, e=8
res=0

0<8:
    volume=1*8-0+1=8
    result=8

    1<7
    start=1

    volume=7*7=49
    result=49
    8>
"""
