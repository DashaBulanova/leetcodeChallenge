import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected", [
([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
([],[]),
([0], []),
([0,0,0,0], [[0,0,0]]),
([3,0,-2,-1,1,2], [[-2,-1,3],[-2,0,2],[-1,0,1]])
])
def test(input, expected):
    actual = Solution().threeSum(input)
    assert actual == expected