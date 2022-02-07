import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, k, expected", [
([1,1,1,0,0,0,1,1,1,1,0], 2, 6),
([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10)
])
def test(nums,k,expected):
    actual = Solution().longestOnes(nums,k)
    assert actual == expected

"""
 0 1 2 3 4 5 6 7 8 9 10
[1,1,1,0,0,0,1,1,1,1,0] k=2
r=result
s=start
e=end

s=0, r=0,
e=0
r=1

e=1
r=2

e=2
r=3

e=3
k=1
r=4

e=4
k=0
r=5

e=5
k=-1
    s=1
    s=2
    s=3
     k=0
    s=4
result=5

e=6,7,8,9,10
k=-1
    s4==0: k=0 s=5


"""