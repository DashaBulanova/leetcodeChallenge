import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected",[
([2,2,1], 1),
([4,1,2,1,2], 4),
([1], 1)
])
def test(input, expected):
    actual = Solution().singleNumber(input)
    assert actual == expected