import pytest

from .solution import Solution


@pytest.mark.parametrize("n, expected", [
    (2, 2),
    (3, 3)
])
def test(n, expected):
    actual = Solution().climbStairs(n)
    assert actual == expected
