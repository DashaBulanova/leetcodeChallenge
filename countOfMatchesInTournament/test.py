import pytest
from .solution import Solution

@pytest.mark.parametrize("n, expected", [
(7, 6),
(14, 13)
])
def test(n, expected):
    actual = Solution().numberOfMatches(n)
    assert actual == expected
