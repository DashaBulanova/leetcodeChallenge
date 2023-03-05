import pytest
from .solution import Solution

@pytest.mark.parametrize("input, target, expected", [
    ([1,3,5,6], 5, 2),
    ([1,3,5,6], 2, 1),
    ([1,3,5,6], 7, 4)
])
def test(input, target, expected):
    actual = Solution().searchInsert(input, target)
    assert actual == expected
