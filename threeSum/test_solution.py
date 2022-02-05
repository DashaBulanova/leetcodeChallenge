import pytest

from .solution import Solution


@pytest.mark.parametrize("input, expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([-1, 0, -4, 1, 2, -1], [[-1, -1, 2], [-1, 0, 1]]),
    ([], []),
    ([0], []),
    ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
    ([0, 0, 0, 0], [[0, 0, 0]])
])
def test(input, expected):
    actual = Solution().threeSum(input)
    assert actual == expected


"""
[-1,0,1,2,-1,-4] 

values = {-1:[0,4], 0:[1], 1:[2], 2:[3], -4:[5]}
i=0
num=-1
res => twoSum(0, 1)
    i=1
    1-0=1 
        j=2
        2!=1 and 2!=0:
            res = [-1,0,1]
    i=2
    1-1=0
    




"""
