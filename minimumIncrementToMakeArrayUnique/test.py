import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, expected",[
	#([1,2,2], 1),
	([3,2,1,2,1,7],6),
	([2,2,2,2,2,2], 15)
])
def test(nums, expected):
	actual = Solution().minIncrementForUnique(nums)
	assert actual == expected

'''
3,2,1,2,1,7
3,2,1,3,2,7 => 2
3,2,1,4,3,7=4
3,2,1,4,4,7=>5
3,2,1,4,5,7=>6

d=3,7,2,1
3,2,4,4,1,7
    | | 
    s e
r=11111

6, min=2 max=2
target: 2,3,4,5,6,7: res=1,2,3,4,5=15
2,2,2,2,2,2
'''