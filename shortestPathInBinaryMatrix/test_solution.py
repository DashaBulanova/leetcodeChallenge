import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected",[
     ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
([[1,0,0],[1,1,0],[1,1,0]], -1),
([[0,1],[1,0]], 2),
([[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]], 14)
])
def test(input, expected):
    actual = Solution().shortestPathBinaryMatrix(input)
    assert actual == expected

"""
0 1 1 0 0 0
0 1 0 1 1 0
0 1 1 0 1 0
0 0 0 1 1 0
1 1 1 1 1 0
1 1 1 1 1 0

clearPathLenght(0,0)
bottom = clearPathLenght(1, 0) => -1
right = clearPathLenght(0, 1) => 3
    b = clearPathLenght(1,1)=>-1
    r = clearPathLenght(0,2)=> 3
        b = clearPathLenght(1,2)=> 2
            b = clearPathLenght(2,2)=>1
            r = -1
            dig = -1
        r = -1
        dig = clearPathLenght(2,2)=> 1
    d = clearPathLenght(1,2)=> 2
        b = clearPathLenght(2,2)=>1
        r = -1
        dig = -1

"""