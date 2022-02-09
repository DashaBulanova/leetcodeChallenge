import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([1, 2, 3, 1], 2),
    ([1, 2, 1, 3, 5, 6, 4], 5),
    ([1], 0),
    ([1, 2], 1)
])
def test(input, expected):
    actual = Solution().findPeakElement(input)
    assert actual == expected


"""
1,2,3,1 
s=0 e=3
mid=0+3//2=1
1<2>3 False

left = find(0,1) = None
    mid=0 
    mid_item = 1
    1 > 2 False
rigth = find(2,3)
    mid=2
    mid_item=3
    

"""
