
"""
[-1,0,1,2,-1,-4]
[-4, -1, -1, 0, 1, 2]
[[-1,-1,2],[-1,0,1]]

i=0
nums=[-4, -1, -1, 0, 1, 2, 2]

prev=None
i=0
twoSum(nums, 1, 4)->
    s=1
    e=5

    -1+2=3 < 4
        s=2
    -1+2=3 <4
        s=3
    0+2<4
        s=4
    1+2<4
        s=5
prev=-4
i=1
twoSum(nums, 2, 1):
    s=2
    e=5
    -1+2=3>1
        e=4
    -1+1=0<1
        s=3
    0+1=1 result=[-1, 0, 1]



"""
import pytest
from solution import Solution

@pytest.mark.parametrize("input, expected", [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([-1,0,1,2,2,-1,-4], [[-4, 2, 2], [-1,-1,2],[-1,0,1]])
])
def test(input, expected):
    actual = Solution().threeSum(input)
    assert actual == expected