import pytest
from .solution import Solution

@pytest.mark.parametrize("arr, expected", [
    ([1,2,2,1,1,3], True),
    ([1,2], False),
    ([-3,0,1,-3,1,1,1,-3,10,0],True)
])
def test(arr, expected):
    actual = Solution().uniqueOccurrences(arr)
    assert actual == expected
