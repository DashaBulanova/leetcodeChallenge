import pytest
from .solution import Solution


@pytest.mark.parametrize(
    "arrays, expected",
    [
        ([[1, 2, 3], [4, 5], [1, 2, 3]], 4),
        ([[-1, 0, 3], [-6, 0]], 9),
        ([[-6, 0, 3], [-1, 0, 1]], 7),
    ],
)
def test(arrays, expected):
    actual = Solution().maxDistance(arrays)
    assert actual == expected
