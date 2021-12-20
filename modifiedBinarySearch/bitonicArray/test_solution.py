# [1, 3, 8, 12, 4, 2]

"""
start=0
end = 6
0<6:
mid = 0+3=3
8<12>4:
retunr 12
"""

"""
[3, 8, 3, 1]
start=0
end = 4
0<4:
mid = 2
8<3>1 false
8<3 false
end = 1

mid=0+0=0
3<8 return 8

"""


"""
[1, 3, 8, 12]
start=0
end=4

mid=2
3<8>12 false
8<12 true => start=3

mid=3
return 
"""
import pytest
from solution import find_max

@pytest.mark.parametrize("input, expected",[
	([1, 3, 8, 12, 4, 2], 12),
	([3, 8, 3, 1], 8),
	([1, 3, 8, 12], 12),
	([10, 9, 8], 10)
	])
def test(input, expected):
	actual = find_max(input)
	assert actual == expected





















