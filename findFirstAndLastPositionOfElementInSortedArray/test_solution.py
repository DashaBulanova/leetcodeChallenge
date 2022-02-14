import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, target, expected",[
([5,7,7,8,8,10], 8, [3,4]),
([5,7,7,8,8,10], 6, [-1,-1]),
([], 0, [-1,-1]),
([1], 1,[0,0])
])
def test(nums, target, expected):
    actual = Solution().searchRange(nums,target)
    assert actual == expected
"""
[5,7,7,8,8,10] target=8
search(0,5)
mid=0+5//2=2
mid_item=7
7<8 search(3,5)=>
    mid=3+1=4
    mid_item=8
    left=search(3,4)=>mid=3 8 => [3,4]
        left=search(3,3)=>[3,3]
        right=search(4,4)=>[4,4]
    right=search(5,5)=>[-1,-1]

"""