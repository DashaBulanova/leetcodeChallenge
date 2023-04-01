import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, target, expected", [ 
    ([-1,0,3,5,9,12], 9, 4),
    ([-1,0,3,5,9,12], 2, -1)
])
def test(nums, target, expected):
    actual = Solution().search(nums, target)
    assert actual == expected
