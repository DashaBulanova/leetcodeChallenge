import pytest
from .solution import Solution

@pytest.mark.parametrize("input, target, expected", [
([2,3,1,2,4,3], 7, 2),
([1,4,4], 4, 1),
([1,1,1,1,1,1,1,1], 11, 0)
    ])
def test(input, target, expected):
    actual = Solution().minSubArrayLen(target, input)
    assert actual == expected

"""
[2,3,1,2,4,3] target=7

start=0

end = 0
acc=2

end=1
acc=5

end=2
acc=6

end=3
acc=8
    result=3-0+1=4
    acc=6
    start=1

end=4
acc=10
    result=min(4, 4-1+1=4)=4
    acc=7
    start=2
    
    result=min(4, 4-2+1=3)=3
    acc=6
    start=3

end=5
acc=9
    result=min(3, 5-3+1=3)=3
    acc=7
    start=4

    result=min(3, 5-4+1=2)=2
    acc=3
    start=5



"""
