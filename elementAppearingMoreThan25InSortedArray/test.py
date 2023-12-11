import pytest
from .solution import Solution

@pytest.mark.parametrize("arr, expected", [
    ([1,2,2,6,6,6,6,7,10], 6),
    ([1,1], 1)
])
def test(arr, expected):
    actual = Solution().findSpecialInteger(arr)
    assert actual == expected
