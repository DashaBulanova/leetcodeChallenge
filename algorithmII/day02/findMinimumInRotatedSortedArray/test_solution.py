import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected",[
	([3,4,5,1,2], 1),
	([4,5,0,1,2], 0),
	([11,13,15,17], 11),
	([4,5,6,7,0,1,2,3,4], 0),
	([0,1,2,4,5,6,7], 0),
	([4,5,6,7,0], 0)
	])
def test(input, expected):
	actual = Solution().findMin(input)
	assert actual==expected

"""
[4, 5, 0, 1, 2]
s=0 e=4
mid=2
4<0<2 false
end=2

mid=0+1=1
4<5<0 false
s=2



[4,5,6,7,0]
s=0 e=4
mid=2

4<6<0
start=2

mid=2+1=3
6<7<0 false
start=3

mid=3+1//2=3
7<=7<0 false
start=4



"""
