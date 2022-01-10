import pytest
from .solution import Solution

@pytest.mark.parametrize("a, b, expected", [
    ("11", "1", "100"),
    ("1010", "1011", "10101")
])
def test(a,b, expected):
    actual = Solution().addBinary(a, b)
    assert actual == expected