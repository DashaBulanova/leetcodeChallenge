import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected",[
([1,2,3,1], 2),
([1,2,1,3,5,6,4], 5),
([1,2],1)
])
def test(input, expected):
    actual = Solution().findPeakElement(input)
    assert actual == expected