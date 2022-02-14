import pytest
from .solution import Solution

@pytest.mark.parametrize("input, target, expected",[
([4,5,6,7,0,1,2], 5, 1),
([4,5,6,7,0,1,2], 0, 4),
([0,1,2,4,5,6,7], 0, 0),
([4,5,6,7,0,1,2], 3, -1),
([1], 1, 0),
([3,1], 1, 1),
([1,3], 3, 1),
([5,1,3], 5,0)
])
def test(input, target, expected):
    actual = Solution().search(input, target)
    assert actual == expected