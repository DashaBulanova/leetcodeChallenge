import pytest
from .solution import Solution

@pytest.mark.parametrize("input, expected", [
(2880, 9),
(1234, 1)
])
def test(input, expected):
    actual = Solution().addDigits(input)
    assert actual == expected