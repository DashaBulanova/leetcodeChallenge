import pytest
from .solution import Solution

@pytest.mark.parametrize("nums, expected", [
([5,2,3,1], [1,2,3,5]),
([5,1,1,2,0,0], [0,0,1,1,2,5])
])
def test(nums, expected):
    actual = Solution().sortArray(nums)
    assert actual == expected
