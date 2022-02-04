import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected",[
([0,1], 2),
([0,1,0], 2),
([0,0,0], 0),
([0,1,1,0,1,1,1,0], 4)
])
def test(input, expected):
    actual = Solution().findMaxLength(input)
    assert actual == expected
"""
[0,1,1,0,1,1,1,0]

i=0
acc=0+1=1
sums={0:-1, 1:0}

i=1
acc = 1-1=0
result=2
sums={0:-1, 1:0}

i=2
acc=-1
sums={0:-1, 1:0, -1:2}

i=3
acc=0
sums={0:-1, 1:0, -1:2}
result=4

i=4
acc=-1
sums={0:-1, 1:0, -1:2}
4-2=2
result=4

i=5
acc=-2
sums={0:-1, 1:0, -1:2, -2:5}
result=4


i=6
acc=-3
sums={0:-1, 1:0, -1:2, -2:5, -3:6}
result=4


i=7
acc=-2
sums={0:-1, 1:0, -1:2, -2:5}
result=4
"""