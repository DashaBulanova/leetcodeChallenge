import pytest
from .solution import Solution

@pytest.mark.parametrize("input,expected",[
([3,4,5,1,2], 1),
([4,5,6,7,0,1,2],0),
([11,13,15,17], 11),
([-4,-3,-1,0,1,3], -4),
([0,1,3,-4], -4)
])
def test(input, expected):
    actual = Solution().findMin(input)
    assert actual == expected

"""
[3,4,5,1,2]
s=0 e=4
mid=2
5<2 False => s=3
mid=3+1//2=3
1<2 True e=3
re
"""