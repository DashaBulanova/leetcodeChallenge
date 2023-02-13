import pytest
from .solution import Solution


@pytest.mark.parametrize("low, high, expected", [
    (3, 7, 3),
    (3, 8, 3),
    (2, 8, 3),
    (8, 10, 1),
    (21, 22, 1),
    (13, 18, 3)
])
def test(low, high, expected):
    actual = Solution().countOdds(low, high)
    assert actual == expected
