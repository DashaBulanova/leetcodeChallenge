import pytest
from .solution import Solution

@pytest.mark.parametrize("input, target, expected",[
([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True),
([[-7,-5,-3,-1],[10,11,16,20],[23,30,34,60]], 13, False),
([[1]], 1, True),
([[1,3,5,7]],3, True)
])
def test(input, target, expected):
    actual = Solution().searchMatrix(input,target)
    assert actual == expected
"""
rs=0,re=2
cs=0,ce=3

rmid=0+(2-0)//2=1
    cmid=0+3//2=1
    matrix=[1][1]=11
    3<11 => ce=1

    cmid=0+1//2=0
    m[1][0]=10
    3<10 => ce=0
    
3<m[1][0]:
re=1
rmid=0+1//2=0
cs,cs=0,3
    cmid=1
    m[0][1]=3 return 3
"""