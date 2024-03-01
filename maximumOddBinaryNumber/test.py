import pytest
from .solution import Solution

@pytest.mark.parametrize("s, expected",[
	("010", "001"),
	("0101", "1001")
])
def test(s, expected):
	actual = Solution().maximumOddBinaryNumber(s)
	assert actual == expected
